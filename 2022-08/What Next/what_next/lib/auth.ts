export type UserCB = ((user: User, error: any) => void) | null;

const crypto = require("crypto");

const userEmail = "admin@example.com";
const userPassword = "changeme";
const key = Buffer.from(
  "56b40075d0d8746b1f63ca0b9f2a9fab3381bbe2366a7fee00c436c6c9e475c5",
  "hex"
);
const algorithm = "aes-256-gcm";

export type User = {
  email: string;
  name: string;
} | null;

export class Auth {
  user: User;

  error: { message: string } | null;

  cb: UserCB = null;

  constructor() {
    this.user = null;
    this.error = null;
  }

  onAuthStateChanged(cb: UserCB) {
    this.cb = cb;

    return () => {
      this.cb = null;
    };
  }

  protected onUserChange(user: User | null, error?: { message: string }) {
    this.cb && this.cb(user, error);
  }

  signIn(email: string, password: string, delay = 2000) {
    console.log(`Sign in with email: ${email} password: ${password}`);

    return new Promise((resolve, reject) => {
      if (email !== userEmail || password !== userPassword) {
        const error = { message: "Wrong email or password" };
        this.error = error;
        reject(error);
        this.onUserChange(null, this.error);

        return;
      }

      setTimeout(() => {
        this.user = {
          name: "Admin",
          email,
        };

        const iv = Buffer.from(crypto.randomBytes(12), "utf8");
        const cipher = crypto.createCipheriv(algorithm, key, iv);
        let enc = cipher.update(JSON.stringify(this.user), "utf8", "base64");
        enc += cipher.final("base64");

        window.sessionStorage.setItem("user", enc);
        window.sessionStorage.setItem("iv", iv.toString("hex"));
        window.sessionStorage.setItem(
          "tag",
          cipher.getAuthTag().toString("hex")
        );
        this.onUserChange(this.user);
        resolve(this.user);
      }, delay);
    });
  }

  signOut() {
    window.sessionStorage.removeItem("user");
    window.sessionStorage.removeItem("iv");
    window.sessionStorage.removeItem("tag");
    this.user = null;
    this.onUserChange(this.user);
  }

  resolveUser(timeout: number) {
    setTimeout(() => {
      if (window) {
        const signedInUser = window.sessionStorage.getItem("user");
        const ivHex = window.sessionStorage.getItem("iv");
        const tagHex = window.sessionStorage.getItem("tag");
        if (signedInUser && ivHex && tagHex) {
          const iv = Buffer.from(ivHex.toString(), "hex");
          const tag = Buffer.from(tagHex.toString(), "hex");
          const decipher = crypto.createDecipheriv(algorithm, key, iv);
          decipher.setAuthTag(tag);

          let str = decipher.update(signedInUser, "base64", "utf8");
          str += decipher.final("utf8");

          this.user = JSON.parse(str);
        }
      } else {
        this.user = null;
      }
      this.onUserChange(this.user);
    }, timeout);

    return this;
  }
}

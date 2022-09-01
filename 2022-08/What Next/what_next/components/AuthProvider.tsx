import React, { useEffect, useState } from "react";
import { Auth, User } from "../lib/auth";

const auth = new Auth(); // singleton

const redirectKey = "sign_in_redirect";

export const AuthContext = React.createContext<
  | {
      auth: Auth;
      initializing: boolean;
      user: User | null;
      error: { message: string };
      setRedirect: (redirect: string) => void;
      getRedirect: () => string | null;
      clearRedirect: () => void;
    }
  | undefined
>(undefined);

AuthContext.displayName = "AuthContext";

function setRedirect(redirect: string) {
  window.sessionStorage.setItem(redirectKey, redirect);
}

function getRedirect(): string | null {
  return window.sessionStorage.getItem(redirectKey);
}

function clearRedirect() {
  return window.sessionStorage.removeItem(redirectKey);
}
export function useAuth() {
  const auth = React.useContext(AuthContext);

  if (!auth) {
    throw new Error("useAuth must be used within AuthProvider");
  }

  return auth;
}

export function AuthProvider({ children }: { children: JSX.Element }) {
  const [user, setUser] = useState<User | null>(null);
  const [error, setError] = useState<{ message: string } | null>(null);
  const [initializing, setInitializing] = useState(true);

  useEffect(() => {
    auth.resolveUser(1000).onAuthStateChanged((user: User, error) => {
      console.log("auth state changed ", user);
      if (user) {
        setUser(user);
        setError(null);
      } else {
        setUser(null);
        if (error) {
          setError(error);
        }
      }
      setInitializing(false);
    });
  }, []);

  const value = {
    user,
    error,
    auth,
    initializing,
    setRedirect,
    getRedirect,
    clearRedirect,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

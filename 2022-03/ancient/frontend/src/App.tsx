import axios from "axios";

import React, { useState, useEffect } from "react";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

interface LoginFormElements extends HTMLFormControlsCollection {
  usernameInput: HTMLInputElement;
  passwordInput: HTMLInputElement;
}

interface LoginFormElement extends HTMLFormElement {
  readonly elements: LoginFormElements;
}

interface PasswordFormElements extends HTMLFormControlsCollection {
  usernameInput: HTMLInputElement;
  passwordInput: HTMLInputElement;
}

interface PasswordFormElement extends HTMLFormElement {
  readonly elements: PasswordFormElements;
}

const LoginForm = ({
  onSubmitLogin,
}: {
  onSubmitLogin: (usernameInput: string, passwordInput: string) => void;
}) => {
  const handleSubmit = (e: React.FormEvent<LoginFormElement>) => {
    e.preventDefault();
    onSubmitLogin(
      e.currentTarget.elements.usernameInput.value,
      e.currentTarget.elements.passwordInput.value
    );
  };
  return (
    <div className="flex flex-col items-center p-4 rounded-b-xl border border-gray-400 w-full">
      <h2 className="font-medium text-4xl mb-4">Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          id="usernameInput"
          type="text"
          placeholder="Username"
          className="text-gray-base w-full py-5 px-4 h-2 border border-gray-300 rounded mb-2"
        />
        <input
          id="passwordInput"
          type="password"
          placeholder="Password"
          className="text-gray-base w-full py-5 px-4 h-2 border border-gray-300 rounded mb-2"
        />
        <button
          type="submit"
          className="w-full bg-blue-600 hover:bg-blue-700 mt-2 py-3 text-lg text-white rounded"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

const PasswordForm = ({
  onSubmitPassword,
}: {
  onSubmitPassword: (usernameInput: string, password: string) => void;
}) => {
  const handleSubmit = (e: React.FormEvent<PasswordFormElement>) => {
    e.preventDefault();
    onSubmitPassword(
      e.currentTarget.elements.usernameInput.value,
      e.currentTarget.elements.passwordInput.value
    );
  };
  return (
    <div>
      <h2 className="font-medium text-4xl mb-4">Get user password</h2>
      <form onSubmit={handleSubmit}>
        <input
          id="usernameInput"
          type="text"
          placeholder="Username"
          className="text-gray-base w-full py-5 px-4 h-2 border border-gray-300 rounded mb-2"
        />
        <input
          id="passwordInput"
          type="password"
          placeholder="Confirm admin Password"
          className="text-gray-base w-full py-5 px-4 h-2 border border-gray-300 rounded mb-2"
        />
        <button
          type="submit"
          className="w-full bg-blue-600 hover:bg-blue-700 mt-2 py-3 text-lg text-white rounded"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

const PasswordDisplay = ({
  username,
  password,
  setPasswordRetrieved,
}: {
  username: string;
  password: string;
  setPasswordRetrieved: (retrieved: boolean) => void;
}) => {
  const handleSubmit = (e: React.SyntheticEvent) => {
    e.preventDefault();
    setPasswordRetrieved(false);
  };
  return (
    <div>
      {password !== undefined ? (
        <p>
          Password for {username} is {password}
        </p>
      ) : (
        <p>Unable to find password for {username}</p>
      )}
      <form onSubmit={handleSubmit}>
        <button
          type="submit"
          className="w-full bg-blue-600 hover:bg-blue-700 mt-2 py-3 text-lg text-white rounded"
        >
          Go Back
        </button>
      </form>
    </div>
  );
};

const PasswordScreen = ({
  username,
  notifyError,
  doLogout,
}: {
  username: string;
  notifyError: (message: string) => void;
  doLogout: () => void;
}) => {
  const [passwordRetrieved, setPasswordRetrieved] = useState<boolean>(false);
  const [passwordRetrievedValue, setPasswordRetrievedValue] =
    useState<string>("");
  const [usernameRetrievedValue, setUsernameRetrievedValue] =
    useState<string>("");

  const doGetPassword = (username: string, password: string) => {
    axios
      .post(
        "/api/admin",
        `<GETPASSWORD><USER>${username}</USER><PASSWORD>${password}</PASSWORD></GETPASSWORD>`,
        {
          headers: {
            "Content-Type": "text/plain",
          },
        }
      )
      .then((response) => {
        console.log(response);
        setPasswordRetrieved(true);
        setUsernameRetrievedValue(response.data.username);
        setPasswordRetrievedValue(response.data.password);
      })
      .catch((error) => {
        if (error.response && error.response.data.error) {
          notifyError(error.response.data.error);
        } else {
          notifyError("Error getting password");
        }
      });
  };

  return (
    <div className="flex flex-col items-center p-4 rounded-b-xl border border-gray-400 w-full">
      <p className="ml-auto">
        Logged in as <span className="font-bold">{username}</span> (
        <button
          className="hover:underline text-black cursor-pointer"
          onClick={doLogout}
        >
          Log out
        </button>
        )
      </p>
      {passwordRetrieved ? (
        <PasswordDisplay
          username={usernameRetrievedValue}
          password={passwordRetrievedValue}
          setPasswordRetrieved={setPasswordRetrieved}
        />
      ) : (
        <PasswordForm onSubmitPassword={doGetPassword} />
      )}
    </div>
  );
};

const App = () => {
  const notifyError = (text: string) =>
    toast.error(text, {
      position: toast.POSITION.TOP_CENTER,
      hideProgressBar: true,
    });

  const [username, setUsername] = useState<string>();
  const [loggedIn, setLoggedIn] = useState<boolean>(false);

  const doLogin = (username: string, password: string) => {
    axios
      .post(
        "/api/login",
        `<LOGIN><USER>${username}</USER><PASSWORD>${password}</PASSWORD></LOGIN>`,
        {
          headers: {
            "Content-Type": "text/plain",
          },
        }
      )
      .then((response) => {
        setLoggedIn(true);
        setUsername(response.data.username);
      })
      .catch((error) => {
        if (error.response && error.response.data.error) {
          notifyError(error.response.data.error);
        } else {
          notifyError("Error logging in");
        }
      });
  };

  const doLogout = () => {
    axios
      .post("/api/logout")
      .then(() => {
        setLoggedIn(false);
        setUsername(undefined);
      })
      .catch(() => {
        setLoggedIn(false);
        setUsername(undefined);
      });
  };

  const getSession = () => {
    axios
      .post("/api/checksession")
      .then((response) => {
        setLoggedIn(true);
        setUsername(response.data.username);
      })
      .catch(() => {});
  };

  useEffect(() => {
    getSession();
  }, []);

  return (
    <div className="h-screen flex flex-col justify-center w-1/3">
      <div className="bg-gray-800 rounded-t-xl w-full">
        <h1 className="font-medium text-5xl mb-4 ml-6 text-white p-4">
          Ancient
        </h1>
      </div>
      {loggedIn && username !== undefined ? (
        <PasswordScreen
          username={username}
          notifyError={(message: string) => notifyError(message)}
          doLogout={doLogout}
        />
      ) : (
        <LoginForm
          onSubmitLogin={(usernameInput, passwordInput) =>
            doLogin(usernameInput, passwordInput)
          }
        />
      )}
      <ToastContainer />
    </div>
  );
};

export default App;

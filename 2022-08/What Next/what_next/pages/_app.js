import "../styles/globals.css";
import { AuthProvider } from "../components/AuthProvider";
import { AuthGuard } from "../components/AuthGuard";

function BlogApp({ Component, pageProps }) {
  return (
    <AuthProvider>
      {Component.requireAuth ? (
        <AuthGuard>
          <Component {...pageProps} />
        </AuthGuard>
      ) : (
        // public page
        <Component {...pageProps} />
      )}
    </AuthProvider>
  );
}

export default BlogApp;

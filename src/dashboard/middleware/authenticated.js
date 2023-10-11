export default function ({ app, redirect }) {
    // Check if the user is authenticated using the Nuxt Auth module
    const isAuthenticated = app.$auth.loggedIn;
  
    if (!isAuthenticated) {
      // If not logged in, redirect to the login page
      redirect('/login');
    }
  }
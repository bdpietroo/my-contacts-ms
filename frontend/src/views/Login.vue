<template>
  <div class="login-page">

    <div class="login-container">
      <div class="login-card">
      <h2>{{ $t('login.title') }}</h2>
        <p>{{ $t('login.description') }}</p>

        <a :href="loginUrl" class="login-button">
          <img
            src="https://docs.microsoft.com/en-us/azure/active-directory/develop/media/howto-add-branding-in-azure-ad-apps/ms-symbollockup_mssymbol_19.svg"
            alt="Microsoft Logo"
          />
          {{ $t('login.button') }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>

const API_BASE_URL = process.env.VUE_APP_API_BASE_URL || 'http://localhost:5000';


export default {
  name: 'LoginView',

  computed: {
    loginUrl() {
      return `${API_BASE_URL}/login`;
    }
  }
};
</script>

<style>

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  background-color: transparent;
}

#app {
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>

<style scoped>

.login-page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;   
  font-family: "Poppins", "Roboto", sans-serif;
  color: #333;
}


.header {
  background-color: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: white;
  text-align: center;
  padding: 1.2rem;
  font-weight: 600;
  letter-spacing: 1px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.logo {
  font-size: 1.6rem;
  margin: 0;
}

.login-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  background: linear-gradient(135deg, #9ac6ec, #91ceff, #6ab5f3);
}

.login-card {
  background: whitesmoke;
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 3rem 2.5rem;
  text-align: center;
  color: #fff;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
  width: 100%;;
  max-width: 420px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;;
}

.login-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
}

h2 {
  color: black;
  font-size: 1.8rem;
  margin-bottom: 0.8rem;
  font-weight: 600;
}

p {
  color: black;
  font-size: 1rem;
  margin-bottom: 2rem;
}

.login-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 14px 26px;
  background-color: #f5f5f5;
  color: #333;
  border-radius: 10px;
  font-weight: 600;
  text-decoration: none;
  font-size: 1rem;
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
  border: solid 1px rgb(67, 67, 67);
}

.login-button:hover {
  border: solid 1px rgba(67, 67, 67, 0.674);
  background-color: #ffffff;
  transform: scale(1.05);
  box-shadow: 0 6px 16px rgba(255, 255, 255, 0.25);
}

.login-button img {
  width: 24px;
  height: 24px;
}

@media (max-width: 480px) {
  .login-card {
    padding: 2rem 1.5rem;
  }

  h2 {
    font-size: 1.4rem;
  }

  p {
    font-size: 0.9rem;
  }

  .login-button {
    padding: 12px 20px;
    font-size: 0.9rem;
  }
}
</style>

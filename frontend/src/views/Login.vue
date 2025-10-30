<template>  
    <div class="card" id="loginCard">
      <div class="card-content">
        <h1>{{ $t('login.title') }}</h1>
        <p>{{ $t('login.description') }}</p>

        <a :href="loginUrl" class="login-button">
          <img
            src="https://docs.microsoft.com/en-us/azure/active-directory/develop/media/howto-add-branding-in-azure-ad-apps/ms-symbollockup_mssymbol_19.svg"
            alt="Microsoft Logo"
          />
          {{ $t('login.button') }}
        </a>
      </div>

      <!-- WAVES ANIMADAS -->
      <div class="waves-wrapper">
        <svg class="waves" viewBox="0 0 1200 200" preserveAspectRatio="none">
          <g class="wave wave1">
            <path d="M0,80 C300,160 900,0 1200,100 L1200,200 L0,200 Z"></path>
          </g>
          <g class="wave wave2">
            <path d="M0,100 C400,200 800,20 1200,120 L1200,200 L0,200 Z"></path>
          </g>
          <g class="wave wave3">
            <path d="M0,90 C200,160 1000,10 1200,100 L1200,200 L0,200 Z"></path>
          </g>
        </svg>
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
    },
  },
};
</script>

<style>
:root {
  --primary-1: #0fc6e5;
  --primary-2: #0ea6c3;
  --primary-3: #07b0c9;
  --card-w: 420px;
}

  *{box-sizing:border-box;margin:0;padding:0}
  html,body{height:100%;font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;}


body {
  margin: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--primary-1);
}


</style>

<style scoped>

/* CARD */
.card {
  position: relative;
  width: var(--card-w);
  background: #fff;
  border-radius: 16px;
  padding: 56px 44px 120px;
  box-shadow: 0 18px 40px rgba(0,0,0,0.12);
  text-align: center;
  overflow: visible;
  z-index: 10;
  transition: transform 0.6s ease, opacity 0.6s ease;
}

.card-content h1 {
  color: var(--primary-2);
  font-size: 26px;
  margin-bottom: 18px;
  font-weight: 800;
}

.card-content p {
  font-size: 16px;
  color: #333;
  margin-bottom: 24px;
}



/* BOTÃO */
.login-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 14px 26px;
  background-color: whitesmoke;
  color: #333;
  border-radius: 10px;
  font-weight: 600;
  text-decoration: none;
  font-size: 1rem;
  transition: transform 0.2s ease;
}

.login-button:hover {
  transform: translateY(-2px);
}

.login-button img {
  width: 24px;
  height: 24px;
}

/* Wrapper do conteúdo do card (para garantir z-index acima das ondas) */
.card-content{ position:relative; z-index:12; }

/* Alinhar as ondas sob o cartão, centralizadas como na primeira imagem */
.waves-wrapper{
  position:absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: -6px;
  width: calc(var(--card-w) + 40px);
  height: 120px;
  overflow:hidden;
  z-index: 6;
  pointer-events:none;
  transition: transform 900ms ease, opacity 500ms ease;
}
.waves-wrapper.up{
  transform: translateX(-50%) translateY(-130%);
  opacity:0;
}
.waves{
  width:100%;
  height:100%;
  display:block;
}
.wave path{ animation:float 6s ease-in-out infinite; transform-origin:center; }

.wave1 path{ fill:var(--primary-1); animation-delay:0s; }
.wave2 path{ fill:var(--primary-2); animation-delay:0.9s; opacity:0.88; }
.wave3 path{ fill:var(--primary-3); animation-delay:1.6s; opacity:0.76; }

@keyframes float{
  0%, 100%{ transform: translateY(0); }
  50%{ transform: translateY(8px); }
}


/* RESPONSIVO */
@media (max-width: 540px) {
  :root { --card-w: 92vw; }
  .card { padding: 36px 20px 110px; width: 92vw; }
  .waves-wrapper { width: calc(92vw + 20px); height: 100px; bottom: -6px; }
  .card-content h1 { font-size: 20px; }
  .card-content p { font-size: 14px; }
  .login-button { padding: 12px 20px; font-size: 0.9rem; }
}
</style>

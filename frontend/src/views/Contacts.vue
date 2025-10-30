<template>
  <body id="bodyContacts" class="bg-blue">
    <header class="topbar">
      <div class="topbar-inner">
        <div class="brand small">
          <img class="logo" src="favicon.png" alt="">
          <div class="title">{{ $t('contacts.header') }}</div>
        </div>
        
        <div class="user-actions">
          <a :href="logoutUrl" class="btn ghost">{{ $t('contacts.logout') }}</a>
        </div>
      </div>
    </header>

    <main class="dashboard-card">
       <p>{{ $t('contacts.subtitle') }}</p>

      <div v-if="loading" class="loading-state">
        <p>{{ $t('contacts.loading') }}</p>
      </div>

      <div v-if="error" class="error-state">
        <p>{{ error || $t('contacts.error') }}</p>
      </div>

      <ContactsTable
        v-if="!loading && !error"
        :contacts="contactsData"
      />
    </main>

  <div class="waves-wrapper small">
    <svg class="waves" viewBox="0 0 1200 240" preserveAspectRatio="none" aria-hidden>
      <g class="wave-group" opacity="0.6">
        <path class="wave wave1" d="M0,120 C150,200 350,20 600,100 C850,180 1050,40 1200,120 L1200,240 L0,240 Z"></path>
      </g>
      <g class="wave-group" opacity="0.4">
        <path class="wave wave2" d="M0,140 C200,60 400,240 600,160 C800,80 1000,220 1200,140 L1200,240 L0,240 Z"></path>
      </g>
      <g class="wave-group" opacity="0.25">
        <path class="wave wave3" d="M0,100 C170,20 370,220 600,120 C830,20 1030,200 1200,100 L1200,240 L0,240 Z"></path>
      </g>
    </svg>
  </div>
  </body>

</template>

<script>
import axios from 'axios';
import ContactsTable from '../components/ContactsTable.vue';

const API_BASE_URL = process.env.VUE_APP_API_BASE_URL || 'http://localhost:5000';

export default {
  name: 'ContactsView',
  components: { ContactsTable },

  data: function () {
    return {
      loading: true,
      error: null,
      contactsData: {}
    };
  },

  computed: {
    logoutUrl: function () {
      return `${API_BASE_URL}/logout`;
    }
  },

  created: function () {
    this.fetchContacts();
  },

  methods: {
    fetchContacts: async function () {
      try {
        const apiUrl = `${API_BASE_URL}/api/contacts`;
        const response = await axios.get(apiUrl, { withCredentials: true });
        
        this.contactsData = response.data;

      } catch (err) {
        this.error = null;
        console.error("Erro ao buscar contatos:", err);

      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style>
#bodyContacts {
  height: 100%;
  background: var(--primary-1);
}

* { 
  box-sizing: border-box;
  margin: 0; 
  padding: 0; }

:root{
  --primary-1: #0fc6e5;
  --bg:#0fc6e5;
  --card:#f5fbfd; 
  --accent:#20b6d6;
  --accent-dark:#0ea6c3;
  --muted:#9bbec7;
  --shadow: rgba(10, 40, 60, 0.18);
  --glass: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(245,250,252,0.95));
  --text:#1d4551;
  font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  font-size: 16px;
}
</style>

<style scoped>

p {
  font-weight: 800;
}

.dashboard-card {
  background-color: #fff;
  border-radius: 16px;
  padding: 2.5rem 2rem;
  max-width: 900px;
  margin: 3rem auto;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.dashboard-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #757575;
}

.error-state {
  color: #d32f2f;
  background-color: #ffebee;
  padding: 1rem;
  border-radius: 8px;
  font-weight: 500;
  margin-bottom: 1.5rem;
}

.bg-blue {
  background: linear-gradient(180deg, rgba(11, 175, 204, 1) 0%, rgba(7, 185, 208, 1) 100%);
  min-height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.bg-blue {
  background: linear-gradient(180deg, rgba(11, 175, 204, 1) 0%, rgba(7, 185, 208, 1) 100%);
  min-height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.brand {
  display:flex;
  flex-direction: column;
  align-items:center;
  gap:12px;
  margin-bottom: 6px;

}
.brand .logo {
  width:64px;
  height:64px;
  border-radius:10px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-weight:700;
  font-size:28px;
  box-shadow: 0 8px 18px rgba(2,120,150,0.18);
}
.brand h1{
  font-weight:600;
  color:var(--accent-dark);
  font-size:18px;
}

.btn { 
  border:0; 
  padding:12px 20px; 
  border-radius:8px; 
  cursor:pointer; 
  font-weight:600; 
  display:inline-flex; 
  align-items:center; 
  gap:10px; 
}

.btn.ghost{
  background:transparent; 
  border:1px solid rgba(255,255,255,0.2); 
  color:white; 
  padding:8px 12px;
}

.waves-wrapper {
  width:100%;
  position:absolute;
  left:0;
  bottom:-10px;
  height:160px;
  z-index:5;
  pointer-events:none;
}
.waves-wrapper.small { 
  bottom: -6px;
  height:120px; 
}

.waves{ 
  width:100%;
  height:100%;
  display:block; 
}

.wave {
  transform-origin: center;
  will-change: transform;
}
.wave1 { fill: rgba(8,173,201,0.95); animation: slide1 9s linear infinite; }
.wave2 { fill: rgba(5,152,188,0.90); animation: slide2 12s linear infinite; }
.wave3 { fill: rgba(0,126,160,0.9); animation: slide3 7s linear infinite; }

@keyframes slide1 {
  0% { transform: translateX(0px) translateY(0); }
  50% { transform: translateX(-40px) translateY(-6px) rotate(-0.2deg); }
  100% { transform: translateX(0px) translateY(0); }
}
@keyframes slide2 {
  0% { transform: translateX(0px) translateY(0); }
  50% { transform: translateX(-80px) translateY(-8px) rotate(0.1deg); }
  100% { transform: translateX(0px) translateY(0); }
}
@keyframes slide3 {
  0% { transform: translateX(0px) translateY(0); }
  50% { transform: translateX(-20px) translateY(-4px) rotate(0.15deg); }
  100% { transform: translateX(0px) translateY(0); }
}

.topbar {
  position: fixed;
  left:0;
  right:0; 
  top:18px;
  display:flex;
  justify-content:center;
  z-index:12;
  pointer-events:none;
}

.topbar-inner {
  width:100%;
  max-width:1100px;
  pointer-events:auto;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:20px;
  padding: 10px 16px;
}

.brand.small { 
  display:flex;
  align-items:center;
  gap:12px;
  color:white; 
}

.brand.small .logo {
  width:40px;
  height:40px;
  font-size:20px;
  box-shadow:none;
}

.title { 
  font-weight:600;
  color:white; 
}

.user-actions { 
  display:flex; 
  align-items:center; 
  gap:12px; 
  color:white; 
}

.dashboard-card {
  width:100%; 
  max-width:920px; 
  background: rgba(255,255,255,0.96); 
  border-radius:8px; padding: 30px;
  box-shadow: 0 18px 30px rgba(2,60,80,0.12);
  border:1px solid rgba(10,60,80,0.03);
}

@media (max-width:880px){
  .card{ padding:28px; }
  .login-card{ padding-bottom:140px; }
  .data-table{ min-width:600px; }
}


</style>
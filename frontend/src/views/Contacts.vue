<template>
  <div class="dashboard-container">

    <header class="app-header">
      <div class="header-content">
        <h1 class="app-title">Bem-vindo à sua área de contatos</h1>
        <a :href="logoutUrl" class="logout-button">Sair</a>
      </div>
    </header>

    <main class="dashboard-card">
       <h3 class="subtitle">Contatos</h3>

      <div v-if="loading" class="loading-state">
        <div class="loader"></div>
        <p>Carregando seus contatos...</p>
      </div>

      <div v-if="error" class="error-state">
        <p>{{ error }}</p>
      </div>

      <ContactsTable
        v-if="!loading && !error"
        :contacts="contactsData"
      />
    </main>

  </div>
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
        
        // A resposta da API (response.data) já é o objeto de contatos que queremos.
        this.contactsData = response.data;

      } catch (err) {
        this.error = 'Falha ao carregar contatos. Tente fazer o login novamente.';
        console.error("Erro ao buscar contatos:", err);

      } finally {
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>

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

.dashboard-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #c7ddf1, #c2e4ff, #85c3f5);
  font-family: 'Roboto', sans-serif;
}

.app-header {
  background-color: #85c3f5;
  color: white;
  padding: 1rem 2rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1000px;
  margin: 0 auto;
}

.app-title {
  font-size: 1.4rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  margin: 0;
}


.logout-button {
  background-color: #ffffff;
  color: #1e88e5;
  padding: 8px 18px;
  border-radius: 8px;
  font-weight: 500;
  text-decoration: none;
  font-size: 0.95rem;
  letter-spacing: 0.3px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.logout-button:hover {
  background-color: #f5f5f5;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.25);
}

.logout-button:active {
  background-color: #eeeeee;
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

.user-greeting {
  color: #1e88e5;
  font-size: 1.6rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: 1.05rem;
  color: #555;
  margin-bottom: 2rem;
}

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: #757575;
}

.loader {
  border: 4px solid #e0e0e0;
  border-top: 4px solid #1e88e5;
  border-radius: 50%;
  width: 36px;
  height: 36px;
  animation: spin 1s linear infinite;
  margin-bottom: 10px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-state {
  color: #d32f2f;
  background-color: #ffebee;
  padding: 1rem;
  border-radius: 8px;
  font-weight: 500;
  margin-bottom: 1.5rem;
}

@media (max-width: 600px) {
  .app-header {
    padding: 0.8rem 1.2rem;
  }

  .app-title {
    font-size: 1.2rem;
  }

  .logout-button {
    padding: 6px 14px;
    font-size: 0.9rem;
  }

  .dashboard-card {
    margin: 2rem 1rem;
    padding: 2rem 1.5rem;
  }

  .user-greeting {
    font-size: 1.4rem;
  }
}
</style>

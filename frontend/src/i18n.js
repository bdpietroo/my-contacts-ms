import { createI18n } from 'vue-i18n';

const messages = {
  'pt-BR': {
    login: {
      title: 'Faça login para começar',
      description: 'Visualize todos os seus contatos da Microsoft agrupados por domínio.',
      button: 'Entrar com a Microsoft'
    },
    contacts: {
      header: 'Bem-vindo à sua área de contatos',
      subtitle: 'Contatos',
      loading: 'Carregando seus contatos...',
      error: 'Falha ao carregar contatos. Tente fazer o login novamente.',
      no_contacts: 'Nenhum contato encontrado ou a lista de contatos está vazia.',
      logout: 'Sair',
      domain: 'Domínio',
      emails: 'E-mails'
    }
  },
  'en': {
    login: {
      title: 'Sign in to start',
      description: 'View all your Microsoft contacts grouped by domain.',
      button: 'Sign in with Microsoft'
    },
    contacts: {
      header: 'Welcome to your contacts area',
      subtitle: 'Contacts',
      loading: 'Loading your contacts...',
      error: 'Failed to load contacts. Try signing in again.',
      no_contacts: 'No contacts found or the contact list is empty.',
      logout: 'Logout',
      domain: 'Domain',
      emails: 'Emails'
    }
  }
};

const i18n = createI18n({
  legacy: false,
  locale: 'pt-BR',
  fallbackLocale: 'en',
  messages
});

export default i18n;
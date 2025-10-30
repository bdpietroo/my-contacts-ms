<template>
  <div class="contacts-table-container">
    
    <!-- Verifica se existem contatos disponíveis para exibição -->
    <table v-if="Object.keys(contacts).length > 0" class="contacts-table">
      <thead>
        <tr>
          <th>{{ $t('contacts.domain') }}</th>
          <th>{{ $t('contacts.emails') }}</th>
        </tr>
      </thead>
      <tbody>
        
        <!-- Itera sobre cada domínio nos contatos -->
        <tr v-for="domain in Object.keys(contacts)" :key="domain">
          <td><strong>{{ domain }}</strong></td>
          <td>
            
            <ul>
              <!-- Itera sobre os e-mails associados ao domínio -->
              <li v-for="email in contacts[domain]" :key="email">
                {{ email }}
              </li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- Mensagem exibida quando não há contatos -->
    <div v-else>
      <p>{{ $t('contacts.no_contacts') }}</p>
    </div>
  </div>
</template>

<script>
/**
 * Este componente exibe a tabela com os contatos organizados por domínio.
 * 
 * Recebe um objeto de contatos via props e renderiza uma tabela
 * agrupado por domínio e-mails
 */
export default {
  name: 'ContactsTable',
  

  props: {
    /** 
   * Objeto de contatos agrupados por domínio
   * A chave é o domínio e o valor é uma lista de e-mails
   */
    contacts: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.contacts-table-container {

  margin: 40px auto;
  max-width: 900px;
  font-family: 'Roboto', sans-serif;
  color: #333;
}

.contacts-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  background-color: #fff;
}

.contacts-table th, .contacts-table td {
  padding: 16px 12px;
}

.contacts-table th {
  background-color: #0ea6c3; 
  color: white;
  font-weight: 500;
  text-align: center; /* títulos centralizados */
  font-size: 16px;
}

.contacts-table tr {
  transition: background-color 0.3s;
}

.contacts-table tr:nth-child(even) {
  background-color: #f5f5f5;
}

.contacts-table tr:hover {
  background-color: #e3f2fd;
}

.contacts-table td {
  font-size: 14px;
}

.contacts-table td:first-child {
  text-align: center; /* domínios centralizados */
}

.contacts-table td:nth-child(2) {
  text-align: left /* emails alinhados à esquerda */
}

.contacts-table ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.contacts-table li {
  padding: 4px 0;
}

</style>
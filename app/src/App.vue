<script>
import ChatContent from './components/ChatContent.vue'
import InputRow from './components/InputRow.vue'
import ReconnectingWebSocket from 'reconnecting-websocket';

export default {
  name: 'App',
  components: {
      ChatContent,
      InputRow,
  },
  data() {
      return {
          messages: [],
          socket: null,
      };
  },
  mounted() {
      this.socket = new ReconnectingWebSocket('ws://localhost:8000/ws');
      this.getMessages();
  },
  methods: {
      getMessages() {

      }
  }
}
</script>

<template>
  <div class="app">
    <div class="app-content">
      <ChatContent />
      <InputRow />
    </div>
  </div>
</template>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
}

.app-content {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  padding: 1rem;
  width: 100%;
  max-width: 1000px;
  overflow: auto;
}
</style>

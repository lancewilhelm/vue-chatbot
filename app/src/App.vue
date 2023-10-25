<script setup>
import ChatContent from './components/ChatContent.vue'
import InputRow from './components/InputRow.vue'
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

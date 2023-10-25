<script>
import ChatBubble from './ChatBubble.vue';

export default {
    name: 'ChatContent',
    components: {
        ChatBubble,
    },
    data() {
        return {
            messages: [],
        };
    },
};
</script>

<template>
    <div class="chat-content">
        <ChatBubble
            v-for="(message, index) in messages"
            :key="index"
            :message="message"
        />
    </div>
</template>

<style scoped>
.chat-content {
    background-color: #f4f8ff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    height: 100%;
    padding: 1rem;
    width: 100%;
    margin-bottom: 10px;
    overflow: auto;
}
</style>

<script>
import ChatBubble from './ChatBubble.vue';

export default {
    name: 'ChatContent',
    components: {
        ChatBubble,
    },
    data() {
        return {
            messages: [
                { role: 'user', content: 'Hello' },
                { role: 'assistant', content: 'Hi, how are you?' },
                { role: 'user', content: "I'm fine, thanks." },
                { role: 'assistant', content: 'Good to hear.' },
                { role: 'user', content: 'Bye.' },
            ],
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
    background-color: #eda9f9;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    height: 100%;
    padding: 1rem;
    width: 100%;
}
</style>

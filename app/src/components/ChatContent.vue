<script>
import ChatBubble from './ChatBubble.vue'

export default {
    name: 'ChatContent',
    components: {
        ChatBubble,
    }
}
</script>

<template>
    <div class='chat-content'>
        <ChatBubble/>
        <ChatBubble/>
        <ChatBubble/>
        <ChatBubble/>
        <ChatBubble/>
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

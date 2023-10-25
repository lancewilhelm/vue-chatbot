<script>
export default {
    name: 'ChatBubble',
    props: {
        message: {
            type: Object,
            required: true,
        },
    },
}
</script>

<template>
<div :class="['chat-bubble', message.role]">
    <div class="chat-bubble-avatar">
        {{ message.role[0].toUpperCase() }}
    </div>
    <div class="chat-bubble-content">
        {{ message.content }}
    </div>
</div>
</template>

<style scoped>
.chat-bubble {
    display: flex;
    align-items: center;
    flex-direction: row;
    margin-bottom: 10px;
}

.chat-bubble.assistant {
    flex-direction: row-reverse;
}

.chat-bubble-avatar {
    flex-shrink: 0;
    background-color: #e1e1e1;
    border-radius: 50%;
    color: #000;
    font-weight: bold;
    height: 40px;
    width: 40px;
    line-height: 40px;
    margin-right: 10px;
    text-align: center;
    margin: 0px 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}

.chat-bubble-content {
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    max-width: 80%;
}

.user .chat-bubble-content {
    background-color: #f6db99;
}

.assistant .chat-bubble-content{
    background-color: #f6f8d0;
}
</style>
    
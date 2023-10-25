<script>
import ChatContent from './components/ChatContent.vue';
import InputRow from './components/InputRow.vue';
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
        this.socket.onmessage = this.handleSocketMessage;
        this.getMessages();
    },
    beforeDestroy() {
        this.socket.close();
    },
    methods: {
        handleSocketMessage(event) {
            const data = JSON.parse(event.data);
            console.log(data);
            if (data.type === 'message_update') {
                this.messages = data.content;
            }
        },
        getMessages() {
            const newMessage = {
                type: 'get_messages',
            };
            this.sendSocketMessage(newMessage);
        },
        sendSocketMessage(message) {
            this.socket.send(JSON.stringify(message));
        },
    },
};
</script>

<template>
    <div class="app">
        <div class="app-content">
            <ChatContent :messages="this.messages"/>
            <InputRow :sendSocketMessage="this.sendSocketMessage" :messages="this.messages"/>
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

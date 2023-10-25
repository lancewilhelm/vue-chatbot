<script>
export default {
    name: 'InputRow',
    components: {
    }
}
</script>

<template>
    <div class='input-row'>
        <textarea rows="3"></textarea>
        <button>Send</button>
    </div>
</template>

<style scoped>
.input-row {
    display: flex;
    align-items: stretch;
    background-color: #fdf0d7;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    padding: 10px;
    width: 100%;
}

textarea {
    flex-grow: 1;
}

.input-row button {
    background-color: #f0e6fb;
    border: none;
    border-radius: 5px;
    padding: 10px;
    cursor: pointer;
    color: #00000089;
    box-shadow: 1px 2px 3px rgba(0, 0, 0, 0.25);
    transition: background-color 0.2s ease-in-out, box-shadow 0.1s ease-in-out;
    margin-left: 10px;
}

button:hover {
    filter: brightness(0.9);
}

button:active {
    box-shadow: none;
}
</style>
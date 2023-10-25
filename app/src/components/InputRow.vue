<script>
export default {
    name: 'InputRow',
    components: {
    }
}
</script>

<template>
    <div class='input-row'>
        <textarea></textarea>
        <button>Send</button>
    </div>
</template>

<style scoped>
.input-row {
    display: flex;
    background-color: #f6db99;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    padding: 1rem;
    width: 100%;
}
</style>
<script setup>
import { nextTick, ref, watch } from 'vue';

const emit = defineEmits(['sendMessage'])

const props = defineProps({
    messages: {
        type: Array,
        required: true
    }
})

watch(props.messages, (newM, oldM) => {
    editor.value.innerHTML = ''
    nextTick(()=>{
        console.log(mscroll.value)
        mscroll.value.scrollTo({
            top: mscroll.value.scrollHeight,
            behavior: "smooth"
        })
    })
})


const editor = ref(null);
const mscroll = ref();

function onSubmit() {
    const text = editor.value.innerText.trim()
    emit('sendMessage', text)
    editor.value.innerHTML = ''
}

</script>

<template>
    <div class="lite-chatmaster">
        <div id="chatBox" class="lite-chatbox" ref="mscroll">
            <div :class="['cmsg', message.position]" v-for="message in messages">
                <img class="headIcon radius" :src="message.icon" />
                <span class="name">{{ message.name }}</span>
                <span class="content">{{ message.content }}</span>
            </div>
        </div>

        <div class="lite-chattools">
            <div class="lite-chatbox-tool" id="emojiMart" style="display:none"></div>
            <div id="toolMusk" style="display:none"></div>
        </div>
        <div class="lite-chatinput">
            <hr class="boundary">

            <div class="editor chatinput" aria-label="input area" contenteditable="true" ref="editor"
                @keyup.enter.exact="onSubmit"></div>
            <button class="send" @click="onSubmit">发送</button>
        </div>
    </div>
</template>

<style scoped>
.lite-chatmaster {
    width: 100%;
}

.chatinput {
    height: 70%;
}
</style>

<script setup>
import { ref } from 'vue';

const emit = defineEmits(['botSelect'])
const props = defineProps({
    bots: {
        type: Array,
        required: true
    }
})


const activeId = ref(0)

function changeActive(index, bot) {
    activeId.value = index
    emit('botSelect', bot)
}
</script>

<template>
    <div class="chat_list">
        <div class="chatListTag" :class="{active: activeId==index}" v-for="(bot, index) in bots" @click="changeActive(index, bot)">
            <div class="head"><img :src="bot.photo" alt=""></div>
            <div class="mytext">
                <div class="name">{{ bot.name }}</div>
                <div class="dec">{{ bot.title }}</div>
            </div>
            <div class="msg_num">{{ bot.messageNum }}</div>
        </div>
    </div>
</template>

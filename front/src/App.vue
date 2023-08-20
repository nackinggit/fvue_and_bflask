<script setup>
import { onMounted, ref } from 'vue';
import BotList from './components/BotList.vue';
import ChatBox from './components/ChatBox.vue';
import PromptEditorPop from './components/PromptEditorPop.vue'
import axios from 'axios';

const bots = ref([])
const messages = ref([])
const selectedBot = ref({})
const showPopFlag = ref(false)

onMounted(() => {
  axios.get('http://localhost:5000/chat_bot/list')
    .then(resp => {
      bots.value = resp.data
      botSelect(resp.data[0])
    })
    .catch(error => {
      alert(error)
    })
})

function botSelect(bot) {
  console.log('select bot: ', bot)
  selectedBot.value = bot
  axios.post('http://localhost:5000/history/chat_bot', { 'bot_name': bot.name })
    .then(resp => {
      console.log(resp.data)
      messages.value = resp.data
    })
    .catch(error => {
      alert(error)
      messages.value = []
    })
}

function sendMessage(text) {
  console.log('send message:', text)
  axios.post('http://localhost:5000/chat', { 'content': text })
    .then(resp => {
      messages.value.push(
        {
          'content': text,
          'position': 'cright',
          'icon': '...',
          'name': 'User'
        })
      messages.value.push(
        {
          'content': resp.data.resp_text,
          'position': 'cleft',
          'icon': '...',
          'name': 'Assistant'
        })
    })
    .catch(error => {
      alert(error)
    })
}

function showPop(botSelect) {
  showPopFlag.value = true
  console.log(showPopFlag)
  console.log(botSelect)
}

function cancelPrompt() {
  showPopFlag.value = false
  console.log('cancel eidt prompt: ')
}

function submitPrompt(bot, editPrompt) {
  showPopFlag.value = false
  console.log('eidt: ', bot)
  console.log('eidt prompt: ', editPrompt)
}
</script>

<template>
  <div class="chat_container">
    <BotList :bots="bots" @bot-select="botSelect" />
    <ChatBox :messages="messages" @send-message="sendMessage" />
    <div class="me_block">
      <div class="myHeadPhoto">
        <img src="sfajh" alt="" />
      </div>
      <div class="myName">123456</div>
      <div class="me_list">
        <div class="item">
          system_prompt:
          <div style="float: right; display: flex;"><a @click="showPop(selectedBot)">点击查看</a></div>
        </div>
      </div>
    </div>
    <PromptEditorPop :bot="selectedBot" :is-show="showPopFlag" @cancel="cancelPrompt" @submit="submitPrompt" />
  </div>
</template>

<style scoped>
.me_block {
  width: 30%;
}
</style>

import './assets/main.css'
import './web_chat_ui/css/style.css'
import './assets/css/litewebchat_input.min.css'
import './assets/css/litewebchat.min.css'


import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')

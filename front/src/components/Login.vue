<script setup>
import { ref } from 'vue';
import axios from 'axios';
import router from '../router';

const uname = ref()
const vcode = ref()

function onSubmit(uname, vcode) {
    console.log('submit', uname, vcode)
    axios.post('http://localhost:5000/chat_bot/login', {'uname': uname, 'vcode': vcode})
    .then(resp => {
        localStorage.setItem('uname', resp.data.uname)
        localStorage.setItem('icon', resp.data.icon)
        router.push('/chat')
    })
}
</script>

<template>
    <div class="box">
        <div>
            <input placeholder="名称" v-model="uname" />
        </div>
        <div>
            <input placeholder="验证码" v-model="vcode" />
        </div>
        <div>
            <button class="login-button" style="float:right" v-on:click="onSubmit(uname, vcode)">登录</button>
        </div>
    </div>
</template>
  
<style  scoped>
.box {
    width: 40%;
    /* height: 40%; */
    position: absolute;
    top: 10%;
    left: 10%;
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
}

input {
    width: 100%;
    padding: 5px 5px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    resize: none;
}

.login-button {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.login-button:hover {
    background-color: #45a049;
}
</style>
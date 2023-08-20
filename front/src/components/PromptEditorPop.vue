<script setup>
import { nextTick, ref, watch } from 'vue';

const emit = defineEmits(['cancel', 'submit'])

const props = defineProps({
    bot: {
        type: Object,
        required: true
    },
    isShow: Boolean
})

const editPrompt = ref()
const myShow = ref(props.isShow)

function cancel() {
    editPrompt.value = ''
    myShow.value = false
    emit('cancel')
}

function submit(bot, prompt) {
    editPrompt.value = ''
    myShow.value = false
    emit('submit', bot, prompt)
}

watch(props.isShow, (newB, oldB) => {
    console.log('watch isShow', newB)
    nextTick(() => {
        editPrompt.value = ''
    })
})

watch(props.bot, (newB, oldB) => {
    console.log('watch bot', newB)
    nextTick(() => {
        editPrompt.value = ''
    })
})
</script>

<template>
    <div class="mask-box" v-show="isShow">
        <div class="box">
            <div>
                <div
                    style="text-align: center; margin-bottom: 20px; margin-top: 20px; font-size: larger; font-style: italic;">
                    {{ bot.name }}
                </div>
                <div class="raw_prompt" style="margin-bottom: 20px; height: 100px; overflow-y: auto;
            border: 1px solid #ccc;border-radius: 8px;">
                    {{ bot.prompt }}
                </div>
                <div style="margin-bottom: 20px; font-size: large; color: gray;">
                    <label for="editPrompt">Edit system prompt:</label>
                </div>
                <textarea name="editPrompt" rows="6" v-model="editPrompt"></textarea>
                <button class="cmb" style="float:right" @click="cancel">取消</button>
                <button class="mb" style="float:right" @click="submit(bot, editPrompt)">确定</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
textarea {
    width: 100%;
    height: 80%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    resize: none;
}

.mask-box {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: rgba(93, 91, 91, 0.751);
}
.mb {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.mb:hover {
    background-color: #45a049;
}

.cmb {
    background-color: grey;
    color: white;
    padding: 14px 20px;
    margin: 8px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.cmb:hover {
    background-color: rgb(191, 190, 190);
}

.box {
    width: 80%;
    height: 80%;
    position: absolute;
    top: 10%;
    left: 10%;
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
}
</style>
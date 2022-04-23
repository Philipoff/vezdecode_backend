<template>
  <div id="app">
    <transition name="fade">
      <div v-if="isLoginKeyValid" key="1" class="child-view">
        <h1 class="text-center">Мемный дашборд</h1>

        <div class="d-flex">
          <div class="top-meme-section pe-2">
            <h2>Топовый мем</h2>
            <div class="top-meme position-relative">
              <img
                  :src="topMeme.photo_url"
                  class="w-100" alt="топ мем!">

              <div class="likes card rounded-pill position-absolute" style="left: 10px; top: 10px">
                {{ topMeme.likes }} лайков
              </div>

              <div class="likes card rounded-pill position-absolute" style="left: 10px; bottom: 10px">
                Автор: {{ topMeme.author }}
              </div>
            </div>
          </div>
          <div class="ml-2">
            <h3>Статистика по мемам</h3>

            <div class="d-flex">
              <div class="card text-center mx-1 d-flex flex-column">
                Всего мемов в базе

                <h2 class="mt-auto">{{ totalMemes }}</h2>
              </div>
              <div class="card text-center mx-1 d-flex flex-column">
                Всего мемов с оценкой

                <h2 class="mt-auto">{{ totalLikes }}</h2>
              </div>
              <div class="card text-center mx-1 d-flex flex-column">
                Всего оценок мемов

                <h2 class="mt-auto">{{ totalMemesWithLikes }}</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="d-flex">
          <div class="meme-card" v-for="meme in memes" :key="meme.photo_url">

          </div>
        </div>
      </div>
      <div v-else class="child-view" key="2">
        <div class="login-modal text-center">
          <h1>Добро пожаловать!</h1>
          <div>
            Для продолжения пожалуйста укажите loginKey
            <div>
              <i>(указан в README.md проекта)</i>
            </div>
          </div>

          <div class="mt-4">
            <input type="text" class="login-key-input" v-bind="loginKey" placeholder="Ваш loginKey">
          </div>

          <div v-show="keyError" style="color: #ff3636; font-size: 12px">
            Произошла ошибка! Некорректный ключ для логина!
          </div>

          <button @click="checkLoginKey" class="mt-4 login-btn">
            Войти!
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>

import axios from "axios";
import {BACKEND} from "@/backend.config";

export default {
  name: 'App',
  components: {},
  data() {
    return {
      loginKey: "",
      isLoginKeyValid: false,
      keyError: false,
      topMeme: null,
      memes: null,
      totalMemes: 0,
      totalLikes: 0,
      totalMemesWithLikes: 0
    }
  },
  methods: {
    checkLoginKey() {
      axios.get(BACKEND + "/check_login_key")
          .then((r) => {
            if (r.data === true) {
              this.isLoginKeyValid = true
            }
          })
          .catch(() => {
            this.isLoginKeyValid = false
            this.keyError = true
          })
    }
  }
}
</script>

<style>
@import "bootstrap-utilities.min.css";
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600&display=swap');

* {
  font-family: 'Rubik', sans-serif;
}

body {
  background: #f4f4f4
}

.login-modal {
  height: 28vh;
  margin-top: calc((100vh - 28vh) / 2);
  width: 30vw;
  margin-left: 35vw;
  padding: 12px;
  border-radius: 30px;
  box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.15);
  background: white;
}

.login-key-input {
  width: 80%;
  font-size: 18px;
  border-radius: 20px;
  padding: 4px 8px;
  border: 1px solid #9d9d9d;
}

.login-btn {
  padding: 8px 20px;
  background: #0d6efd;
  border-radius: 100px;
  font-size: 20px;
  color: white;
  transition: all .3s ease;
  cursor: pointer;
  border: none;
}

.login-btn:hover {
  background: #0a58ca;
}

.card {
  padding: 14px;
  border-radius: 30px;
  box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.15);
  background: white;
}

.top-meme {
  overflow: hidden;
  box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.15);
  border-radius: 30px;
}

.top-meme img {
  object-fit: cover;
}

.top-meme-section {
  max-width: 30vw;
}
</style>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity .3s ease
}

.fade-enter, .fade-leave-active {
  opacity: 0;
}

.child-view {
  position: absolute;
  transition: all .3s cubic-bezier(.55, 0, .1, 1);
}
</style>

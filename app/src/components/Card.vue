<template>
  <div class="card">
    <textarea v-if="edit"
           @blur.native="valueLocal = $event.target.data; edit = false; $emit('input', valueLocal);"
           @keyup.enter.native="valueLocal = $event.target.data; edit = false; $emit('input', valueLocal);"
           v-focus="">
       {{ valueLocal }}
      </textarea>
    <div v-else class="card-body" @click="edit = true;">
      <h5 class="card-title">{{ data.title }}</h5>
      <!-- id: {{ card.id }} -->
      <p class="card-text">{{ data.text }}</p>
      <pre class="card-data">{{ data }}</pre>
    </div>
  </div>
</template>

<script>
export default {
  props: ['data'],
  data () {
    return {
      edit: false,
      valueLocal: this.data
    }
  },

  watch: {
    value: function () {
      this.valueLocal = this.data
    }
  },

  directives: {
    focus: {
      inserted (el) {
        el.focus()
      }
    }
  }
}
</script>
<template>
  <div class="card">
    <div class="edit-card" 
        v-if="(edit || isAdding)">
      <form>
        <span v-if="isAdding"
        <input type="hidden" name="card_id" 
        :value="this.id" v-if="this.id" != undefined
         />
        <table class="table card-inputs card" >
          <tr v-model="kvstore"
            v-bind:key="index" v-for="(keyvalue, index) in kvstore" >
        <td><input v-on:keyup.enter="setCard" @blur="setCard" type="text" :value="keyvalue.cardkey" /></td>
        <td><input type="text" :value="keyvalue.cardvalue" /></td>
        <td><a @click="deleteRow(index)" class="btn btn-warning" >Delete</a></td>
        </tr>
        <p><a class="btn btn-info" @click="addRow">Add</a></p>
        <p>
        <a class="btn btn-success" @click="setCard">Validate</a>
        <a class="btn btn-danger" @click="delCard" >Delete card</a>
        <!-- <a class="btn btn-danger" @click="delCard" @@@@confirm@@@@ >Delete card</a> -->
</p>
        </table>
      </form>
    </div>
      <table v-else @click="edit = true;" class="card display-card table table-sm table-striped">
        <tr v-for="(cardvalue, cardkey) in kvstore">
          <td>
            <i>{{ cardkey }}</i>
          </td>
          <td>{{ cardvalue }}</td>
        </tr>
      </table>
        <p class="card"><pre class="card-kvstore">{{ kvstore }}</pre></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: {
    kvstore: {
      type: Array,
      // type: Object,
      default: function () { return [{'name': ''}] }

    },
    keyvalue: {
      type: Object,
      default: function () { return {'cardkey': '', 'cardvalue': ''} }
    },
    isAdding: Boolean
  },
  data () {
    return {
      // isAdding: false,
      // kvstore: {
      //   type: Array,
      //   default: function () { return {'': ''} }

      // },
      id: '',
      // card: {'kvstore': {'title': ''}},
      edit: false,
      index: 0
    }
  },

  methods: {
    getCard () {
      const path = `http://localhost:5000/api/cards/`
      var request
      if (this.isAdding !== 'true') {
        request = path + this.id
      }
      axios.get(request)

        .then(response => {
          this.id = response.data.id
          this.kvstore = response.data.kvstore
        })
        .catch(error => {
          console.log(error)
        })
    },

    setCard () {
      const path = `http://localhost:5000/api/cards/`
      var request = path
      // if (this.isAdding !== true) {
      if (this.isAdding !== 'true') {
        request = path + this.id
      }
      axios
        .post(request, this.kvstore)
        .then(response => {
          if (this.isAdding) { this.isAdding = !(response.status === 200) }
        })
        .catch((error) => {
          console.log(error)
        })

      // this.edit = false
    },
    delCard () {},
    addRow () {
      this.kvstore.push('hello')
    },
    deleteRow (index) {
      this.kvstore.splice(index, 1)
    }
  },
  updated () {
    this.setCard()
    this.getCard()
  }
  // computed: {
  //   keyname: function (key) {
  //     return 'key-' + key
  //   },
  //   valuename: function (key, value) {
  //     return 'value-' + value
  //   }
  // },
  // mounted () {
  //   // var doc = jsyaml.load('greeting: hello\nname: world');
  //   this.jsonString =
  //     typeof this.card !== 'undefined' ? JSON.stringify(this.card.data) : '{}'
  //   // this.jsonString = JSON.stringify(this.card.data)
  // },
  // watch: {
  //   data: function (newValue) {
  //     try {
  //       this.data = newValue
  //     } catch (err) {
  //       console.log('seems to be invalid: ' + err)
  //       // reset:
  //       // this.jsonString = JSON.stringify(this.card.data)
  //     }
  //   }
  // }
  // directives: {
  //  focus: {
  //    inserted (el) {
  //      el.focus()
  //    }
  //  }
  // }
}
</script>
<template>
    <div>
        <b-container>
            <b-row>
                <b-col sm="2">
                    Page {{ currentPage }} of {{ totalPages }}, showing {{ fromItems }} - {{ toItems }} of {{ total }}
                    items.
                </b-col>
                <b-col sm="1">
                    <b-button id="prev-page" @click="prevPage" :disabled="!canGoBack">&#8592;Back</b-button>
                </b-col>
                <b-col sm="1">
                    <b-button id="next-page" @click="nextPage" :disabled="!canGoNext">Next&#8594;</b-button>
                </b-col>
                <b-col sm="3">
                    <b-form-input v-model="search" placeholder="Search Author"></b-form-input>
                </b-col>
                <b-col sm="3">
                    <b-button id="show-btn" @click="addAuthor">Add Author</b-button>
                </b-col>
            </b-row>
        </b-container>

        <b-table striped hover :items="items" :fields="fields" @row-clicked="onRowClicked"></b-table>
        <b-modal ref="add-author" hide-footer title="Add New Author">
            <b-row>
                <b-col sm="3">
                    <label :for="author_name">Name:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input :id="author_name" v-model="author_name" placeholder="Author Name"></b-form-input>
                </b-col>
            </b-row>
            <b-row>
                <b-button id="save-author" @click="saveAuthor">Add Author</b-button>
            </b-row>
        </b-modal>

        <b-modal ref="edit-modal" hide-footer title="Edit Author">
            <b-row>
                <b-col sm="3">
                    <label :for="author_name">Name:</label>
                </b-col>
                <b-col sm="9">
                    <b-form-input :id="author_name" v-model="author_name" placeholder="Author Name"></b-form-input>
                </b-col>
            </b-row>
            <b-row>
                <books :parent_author_id="this.author_id"></books>
            </b-row>
            <b-row>
                <b-button id="save-author" @click="patchAuthor">Save Author</b-button>
            </b-row>
        </b-modal>

    </div>
</template>

<script>

import books from './books.vue'
export default {
    middleware: 'authenticated',
    components: { books },
    data() {
        return {
            items: [],
            fields: ["name", "number_books"],
            search: "",
            limit: 10,
            offset: 0,
            total: 0,
            author_id: 0,
            author_name: ""
        }

    },
    methods: {
        nextPage() {
            if (this.canGoNext) {
                this.offset = this.offset + this.limit
                this.$fetch()
            }
        },
        prevPage() {
            if (this.canGoBack) {
                this.offset = this.offset - this.limit
                this.$fetch()
            }
        },
        showModal(modalId) {
            this.$refs[modalId].show()
        },
        hideModal(modalId) {
            this.$refs[modalId].hide()
        },
        addAuthor(){
            this.author_name = ""
            this.showModal('add-author')
        },
        async saveAuthor() {
            this.hideModal('add-author')
            console.log('author_name', this.author_name)
            try {
                let response = await this.$axios.$post("/authors", { name: this.author_name })
                this.$fetch()
            } catch (error) {
                console.log(error)
            }
        },

        async patchAuthor() {
            this.hideModal('edit-modal')
            try {
                let response = await this.$axios.$patch(`/authors/${this.author_id}`, { id: this.author_id, name: this.author_name })
                this.$fetch()
            } catch (error) {
                console.log(error)
            }
        },
        async onRowClicked(item) {
            this.author_id = item.id
            this.author_name = item.name
            this.showModal('edit-modal')
            console.info(item)
        },
    },
    computed: {
        currentPage() {
            return Math.floor(this.offset / this.limit) + 1
        },
        totalPages() {
            return Math.ceil(this.total / this.limit)
        },
        fromItems() {
            return this.offset + 1
        },
        toItems() {
            return Math.min(this.offset + this.limit, this.total)
        },
        canGoBack(){
            return this.offset - this.limit >= 0
        },
        canGoNext(){
            return this.offset + this.limit < this.total
        }
    },

    async fetch() {
        let { items, limit, offset, total } = await this.$axios.$get(`/authors?limit=${this.limit}&offset=${this.offset}&search=${this.search}`)
        this.items = items
        this.limit = limit
        this.offset = offset
        this.total = total
    },
    watch: {
        search(newSearch, oldSearch) {
            this.$fetch()
        }
    }
}

</script>

<style scoped>
.row {
    justify-content: space-between;
    align-items: center;
}
    
</style>
<template>
  <div style="flex-direction: column;">
    <header style="flex-direction: row; margin-left: 30px">
      <RuTubeLogo style="height: 25%;" />
      <h2 style="font-size: 40px;">RecSys</h2>
    </header>
    <div class="grid-container">
      <VideoCard v-for="card in videos" :key="card.video_id" :video_data="card" />
    </div>
  </div>

</template>

<script lang="ts">
import { useHomePageStore } from '@/stores/homepage'
import VideoCard from '@/components/VideoCard.vue';
import Video from '@/interfaces/video';
import RuTubeLogo from '@/assets/Minilogo_RUTUBE_white_mono.svg';
import axios from 'axios';

let store;
export default {
  components: {
    VideoCard,
    RuTubeLogo
  },
  created() {
    this.authorize();
    this.fetchVideos();
  },
  data() {
    return {
      videos: [] as Video[]
    };
  },

  methods: {
    async authorize() {
      try {
        const session_id = await localStorage.getItem('session_id');
        if (session_id === null)
        {
          const response = await axios.get('http://127.0.0.1:8000/api/authorize');
          localStorage.setItem('session_id', response.data.session_id);
        } else {
          const response = await axios.get(`http://127.0.0.1:8000/api/authorize?session_id=${session_id}`);
          localStorage.setItem('session_id', response.data.session_id);
        }

      } catch (err) {
        this.error = `Error fetching videos: ${err.message}`;

      }
    },
    async fetchVideos() {
      store = useHomePageStore();
      try {
        const session_id = await localStorage.getItem('session_id');
        const response = await fetch(`http://127.0.0.1:8000/api/videos_data?session_id=${session_id}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        store.setVideos(await response.json());
        this.videos = store.videos;
      } catch (err) {
        this.error = `Error fetching videos: ${err.message}`;
      }
    },
  }
};

</script>
<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 50px;
  padding: 20px;
  width: 80vw;
  margin: 0 auto;
}
</style>

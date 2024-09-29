import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


export const useHomePageStore = defineStore('homepage', {
    state: () => {
        return {
            videos: []
        }
    },
    actions: {
        setVideos(videos) {
            this.videos = videos
        },
        likeVideo(video_id: string) {
            for (let i = 0; i < this.videos.length; i++) {
                if (this.videos[i].video_id == video_id) {
                    this.videos[i].liked = true;
                    this.videos[i].v_likes++;
                    this.videos[i].disliked = false;
                    break;
                }
            }
        },
        dislikeVideo(video_id: string) {
            for (let i = 0; i < this.videos.length; i++) {
                if (this.videos[i].video_id == video_id) {
                    this.videos[i].liked = false;
                    this.videos[i].v_dislikes++;
                    this.videos[i].disliked = true;
                    break;
                }
            }
        }
    }
})

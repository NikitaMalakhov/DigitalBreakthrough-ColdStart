interface Video {
    liked: boolean;
    disliked: boolean;
    video_id: string;                     // Unique identifier for the video
    v_pub_datetime: string;               // Publication date and time
    v_total_comments: number;             // Total number of comments
    v_year_views: number;                 // Views in a year
    v_month_views: number;                // Views in a month
    v_week_views: number;                 // Views in a week
    v_day_views: number;                  // Views in a day
    v_likes: number;                      // Number of likes
    v_dislikes: number;                   // Number of dislikes
    v_duration: number;                   // Duration of the video (presumably in seconds)
    v_cr_click_like_7_days: number;      // Clicks on like in the last 7 days
    v_cr_click_dislike_7_days: number;   // Clicks on dislike in the last 7 days
    v_cr_click_vtop_7_days: number;      // Clicks on video top in the last 7 days
    v_cr_click_long_view_7_days: number; // Clicks on long view in the last 7 days
    v_cr_click_comment_7_days: number;   // Clicks on comment in the last 7 days
    v_cr_click_like_30_days: number;     // Clicks on like in the last 30 days
    v_cr_click_dislike_30_days: number;  // Clicks on dislike in the last 30 days
    v_cr_click_vtop_30_days: number;     // Clicks on video top in the last 30 days
    v_cr_click_long_view_30_days: number; // Clicks on long view in the last 30 days
    v_cr_click_comment_30_days: number;  // Clicks on comment in the last 30 days
    v_cr_click_like_1_days: number;      // Clicks on like in the last 1 day
    v_cr_click_dislike_1_days: number;   // Clicks on dislike in the last 1 day
    v_cr_click_vtop_1_days: number;      // Clicks on video top in the last 1 day
    v_cr_click_long_view_1_days: number; // Clicks on long view in the last 1 day
    v_cr_click_comment_1_days: number;   // Clicks on comment in the last 1 day
    v_is_hidden: number;                  // Flag indicating if the video is hidden
    v_is_deleted: number;                 // Flag indicating if the video is deleted
    v_avg_watchtime_1_day: number;       // Average watch time in the last 1 day
    v_avg_watchtime_7_day: number;       // Average watch time in the last 7 days
    v_avg_watchtime_30_day: number;      // Average watch time in the last 30 days
    v_frac_avg_watchtime_1_day_duration: number; // Fraction of average watch time to duration in the last 1 day
    v_frac_avg_watchtime_7_day_duration: number; // Fraction of average watch time to duration in the last 7 days
    v_frac_avg_watchtime_30_day_duration: number; // Fraction of average watch time to duration in the last 30 days
    v_category_popularity_percent_7_days: number; // Category popularity percentage in the last 7 days
    v_category_popularity_percent_30_days: number; // Category popularity percentage in the last 30 days
    v_long_views_1_days: number;        // Long views in the last 1 day
    v_long_views_7_days: number;        // Long views in the last 7 days
    v_long_views_30_days: number;       // Long views in the last 30 days
    row_number: number;                 // Row number in the dataset
    title: string;                      // Title of the video
    description: string;                // Description of the video
    category_id: string;                // Category ID of the video
    author_id: string;                  // Author ID of the video
}

export default Video;
SELECT DISTINCT LEAST(liker_id, liked_id) AS user1_id,
                GREATEST(liker_id, liked_id) AS user2_id
FROM user_likes
WHERE (liker_id, liked_id) IN (SELECT liked_id, liker_id FROM user_likes)
ORDER BY user1_id, user2_id;

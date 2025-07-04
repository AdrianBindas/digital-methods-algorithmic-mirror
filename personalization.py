from datetime import datetime
import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def load_ndjson(fle, subkey=None):

    json_lst = []

    with open(fle, "r") as file:
        for line in file:
            dp = json.loads(line)
            if subkey:
                json_lst.append(dp[subkey])
            else:
                json_lst.append(dp)

    return json_lst


def segment_df_per_time(df_in, timekey, start_time, end_time):
    df = df_in.copy()

    df[timekey] = pd.to_datetime(df[timekey])
    df.set_index(timekey, inplace=True)
    df.sort_index(inplace=True)

    time_segment = df[start_time:end_time]

    return time_segment


def plot_over_time(*args):
    if len(args) % 2 != 0:
        raise ValueError("The number of arguments should be even: pairs of data and description.")

    def extract_dates(list_of_dicts):
        extracted_dates = []
        for item in list_of_dicts:
            date_value = item["Date"]
            # Check if the date_value is already a datetime object
            if isinstance(date_value, datetime):
                extracted_dates.append(date_value)
            else:
                # Convert the string to a datetime object
                extracted_dates.append(datetime.strptime(date_value, "%Y-%m-%d %H:%M:%S"))
        return extracted_dates

    # Initialize a list to hold DataFrames
    dfs = []

    # Loop over pairs of data and descriptions
    for i in range(0, len(args), 2):
        data = args[i]
        desc = args[i + 1]

        # Extract dates and create DataFrame
        dates = extract_dates(data)
        df = pd.DataFrame({'Date': dates, 'List': desc})
        dfs.append(df)

    # Combine all DataFrames
    combined_df = pd.concat(dfs, ignore_index=True)

    # Plot using Seaborn
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=combined_df, x='Date', y='List', hue='List', palette='viridis')
    plt.title('Plot of Dates Over Time')
    plt.xlabel('Date')
    plt.ylabel('List')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    # LOAD DATA
    # gdpr data
    gdpr_df_out = pd.read_json("data/archetypes/optout/gdpr_data_after_round2/user_data_tiktok.json")
    gdpr_df_in = pd.read_json("data/archetypes/optin/gdpr_data_after_round2/user_data_tiktok.json")
    favs_out = pd.DataFrame(gdpr_df_out["Your Activity"]["Favorite Videos"]["FavoriteVideoList"])
    favs_in = pd.DataFrame(gdpr_df_in["Your Activity"]["Favorite Videos"]["FavoriteVideoList"])

    # zeeschuimmer data
    posts_scroll_1_out = pd.DataFrame(load_ndjson("data/archetypes/optout/browsing_videos.ndjson"))
    posts_scroll_1_out["Date"] = pd.to_datetime(posts_scroll_1_out["timestamp_collected"], unit="ms")
    posts_scroll_1_in = pd.DataFrame(load_ndjson("data/archetypes/optin/browsing_videos.ndjson"))
    posts_scroll_1_in["Date"] = pd.to_datetime(posts_scroll_1_in["timestamp_collected"], unit="ms")
    posts_scroll_2_out = pd.DataFrame(load_ndjson("data/archetypes/optout/browsing_round2_posts.ndjson"))
    posts_scroll_2_out["Date"] = pd.to_datetime(posts_scroll_2_out["timestamp_collected"], unit="ms")
    posts_scroll_2_in = pd.DataFrame(load_ndjson("data/archetypes/optin/browsing_round2_posts.ndjson"))
    posts_scroll_2_in["Date"] = pd.to_datetime(posts_scroll_2_in["timestamp_collected"], unit="ms")

    # plot_over_time(posts_scroll_1.to_dict(orient="records"), "Collection timestamps")

    # segment
    # seeding
    # seeding_out = segment_df_per_time(favs_out, "Date", "2025-07-02 07:47:11", "2025-07-02 09:05:00")
    # print("SEEDING OUT")
    # print(seeding_out)
    # seeding_in = segment_df_per_time(favs_in, "Date", "2025-07-02 07:47:11", "2025-07-02 09:05:00")
    # print("SEEDING IN")
    # print(seeding_in)

    # COUNT FREQUENCIES
    print(f"TOTAL FAVS OUT {len(favs_out)}")
    print(f"TOTAL FAVS IN {len(favs_in)}")
    round1_out_favs = segment_df_per_time(favs_out, "Date", "2025-07-02 10:00:00", "2025-07-02 11:00:00")
    round1_out_watched = posts_scroll_1_out # from zeeschuimmer cos no watchlist in gdpr yet
    print("[ROUND 1] OUT")
    print(f"{len(round1_out_favs)}/{len(round1_out_watched)}")
    perc = (len(round1_out_favs)/len(round1_out_watched))*100
    print(perc)
    round1_in_favs = segment_df_per_time(favs_in, "Date", "2025-07-02 10:00:00", "2025-07-02 11:00:00")
    round1_in_watched = posts_scroll_1_in
    print("[ROUND 1] IN")
    print(f"{len(round1_in_favs)}/{len(round1_in_watched)}")
    perc = (len(round1_in_favs)/len(round1_in_watched))*100
    print(perc)


    round2_out_favs = segment_df_per_time(favs_out, "Date", "2025-07-03 07:47:00", "2025-07-03 09:00:00")
    round2_out_watched = posts_scroll_2_out
    print("[ROUND 2] OUT")
    print(f"{len(round2_out_favs)}/{len(round2_out_watched)}")
    perc = (len(round2_out_favs)/len(round2_out_watched))*100
    print(perc)
    round2_in_favs = segment_df_per_time(favs_in, "Date", "2025-07-03 07:47:00", "2025-07-03 09:00:00")
    round2_in_watched = posts_scroll_2_in
    print("ROUND 2 IN")
    print(f"{len(round2_in_favs)}/{len(round2_in_watched)}")
    perc = (len(round2_in_favs)/len(round2_in_watched))*100
    print(perc)
    # plot_over_time(gdpr_df_out["Your Activity"]["Favorite Videos"]["FavoriteVideoList"], "GDPR", posts_scroll_1.to_dict(orient="records"), "Round 1", posts_scroll_2.to_dict(orient="records"), "Round 2")

    def extract_last_part(url):
        return url.rstrip("/").split('/')[-1]

    # COMBINE GDPR (FAVOURITES) AND ZEESCHUIMER DATA (WATCHED VIDEOS)
    round1_out_favs["fav"] = 1
    round1_out_favs.reset_index(inplace=True)
    round1_out_favs["vid_id"] = round1_out_favs["Link"].apply(extract_last_part)
    round1_out_favs.rename(columns={"Date": "timestamp"}, inplace=True)

    round1_out_watched["fav"] = 0
    round1_out_watched["vid_id"] = round1_out_watched["item_id"].apply(extract_last_part)
    round1_out_watched.rename(columns={"Date": "timestamp"}, inplace=True)

    round1_out = pd.concat([round1_out_favs, round1_out_watched[["vid_id", "timestamp", "fav"]]])
    round1_out["vid_id"] = round1_out["vid_id"].astype(int)
    round1_out["round"] = 1
    # drop duplicates
    print(round1_out)
    round1_out = round1_out.sort_values(by="fav", ascending=False)
    round1_out = round1_out.drop_duplicates(subset="vid_id", keep="first")
    round1_out.sort_values(by="timestamp", inplace=True)
    round1_out['order'] = range(1, len(round1_out) + 1)
    print(round1_out)

    round2_out_favs["fav"] = 1
    round2_out_favs.reset_index(inplace=True)
    round2_out_favs["vid_id"] = round2_out_favs["Link"].apply(extract_last_part)
    round2_out_favs.rename(columns={"Date": "timestamp"}, inplace=True)

    round2_out_watched["fav"] = 0
    round2_out_watched["vid_id"] = round2_out_watched["item_id"].apply(extract_last_part)
    round2_out_watched.rename(columns={"Date": "timestamp"}, inplace=True)

    round2_out = pd.concat([round2_out_favs, round2_out_watched[["vid_id", "timestamp", "fav"]]])
    round2_out["vid_id"] = round2_out["vid_id"].astype(int)
    round2_out["round"] = 2
    print(round2_out)
    # drop duplicates
    round2_out = round2_out.sort_values(by="fav", ascending=False)
    round2_out = round2_out.drop_duplicates(subset="vid_id", keep="first")
    round2_out.sort_values(by="timestamp", inplace=True)
    round2_out['order'] = range(1, len(round2_out) + 1)
    print(round2_out)
    opted_out_combined = pd.concat([round1_out, round2_out])
    print(opted_out_combined)
    opted_out_combined.to_csv("data/archetypes/optout/opted_out_timeline.csv", index=False)

    # ROUND 1 OPT IN
    round1_in_favs["fav"] = 1
    round1_in_favs.reset_index(inplace=True)
    round1_in_favs["vid_id"] = round1_in_favs["Link"].apply(extract_last_part)
    round1_in_favs.rename(columns={"Date": "timestamp"}, inplace=True)

    round1_in_watched["fav"] = 0
    round1_in_watched["vid_id"] = round1_in_watched["item_id"].apply(extract_last_part)
    round1_in_watched.rename(columns={"Date": "timestamp"}, inplace=True)

    round1_in = pd.concat([round1_in_favs, round1_in_watched[["vid_id", "timestamp", "fav"]]])
    round1_in["vid_id"] = round1_in["vid_id"].astype(str)
    round1_in["round"] = 1
    # drop duplicates
    print(round1_in)
    round1_in = round1_in.sort_values(by="fav", ascending=False)
    round1_in = round1_in.drop_duplicates(subset="vid_id", keep="first")
    round1_in.sort_values(by="timestamp", inplace=True)
    round1_in['order'] = range(1, len(round1_in) + 1)
    print(round1_in)

    round2_in_favs["fav"] = 1
    round2_in_favs.reset_index(inplace=True)
    round2_in_favs["vid_id"] = round2_in_favs["Link"].apply(extract_last_part)
    round2_in_favs.rename(columns={"Date": "timestamp"}, inplace=True)

    round2_in_watched["fav"] = 0
    round2_in_watched["vid_id"] = round2_in_watched["item_id"].apply(extract_last_part)
    round2_in_watched.rename(columns={"Date": "timestamp"}, inplace=True)

    round2_in = pd.concat([round2_in_favs, round2_in_watched[["vid_id", "timestamp", "fav"]]])
    round2_in["vid_id"] = round2_in["vid_id"].astype(str)
    round2_in["round"] = 2
    print(round2_in)
    # drop duplicates
    round2_in = round2_in.sort_values(by="fav", ascending=False)
    round2_in = round2_in.drop_duplicates(subset="vid_id", keep="first")
    round2_in.sort_values(by="timestamp", inplace=True)
    round2_in['order'] = range(1, len(round2_in) + 1)
    print(round2_in)
    opted_in_combined = pd.concat([round1_in, round2_in])
    print(opted_in_combined)
    opted_in_combined.to_csv("data/archetypes/optin/opted_in_timeline.csv", index=False)


if __name__ == "__main__":
    main()

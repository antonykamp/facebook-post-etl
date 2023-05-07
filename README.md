# Facebook Post ETL

This ETL (Extract, Transform, Load) tool is used to scrape Facebook posts of a certain user, filter them by their and save them as txt files.

## Command Line Interface

You can run the ETL tool by executing the following command:

```bash
python etl.py
```

The following arguments are available:

| Argument           | Description                                                                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--scraped_posts`  | Path to a file containing the scraped posts. If the file doesn't exists, then It tries to scrape a specified number of post from the user specified. Afterwards it saves the post in the file. |
| `--username`       | Username of the Facebook user whose posts should be scraped.                                                                                                                                   |
| `--min_num_words`  | Minimum number of words a post should have to be saved.                                                                                                                                        |
| `--cookies`        | Path to the file containing cookies for the `facebook_scraper` tool. You can find more information [here](https://github.com/kevinzg/facebook-scraper#optional-parameters).                    |
| `--search_token`   | A number of search keywords to filter the posts.                                                                                                                                               |
| `--filtered_posts` | Path to a directory where the filtered posts should be saved as txt files.                                                                                                                     |

## Extract

In the extract step the Facebook posts are scraped using the [facebook-scraper](https://github.com/kevinzg/facebook-scraper) tool.

Specify with `--scraped_posts` argument the path to the file, where you want to save the scraped post to. In the future it tries to reuse the saved posts.

## Transform

In the transform step it filters the collected posts by their content.
You can specify the search tokens to filter with the `--search_token` argument.

## Load

In the load step the filtered posts are saved as txt files in the directory specified by the `--filtered_posts` argument.

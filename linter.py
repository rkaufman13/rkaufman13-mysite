import os
from html.parser import HTMLParser

REQUIRED_ATTRS_FOR_VIDEO = ['playsinline','muted']
class DisallowedAttributeException(BaseException):
    def __init__(self, attr, tag, filename):
        message = f"We don't allow {attr[0]} in {tag} round these parts. Check {filename} for more info"
        super().__init__(message)

class MissingAttributeException(BaseException):
    def __init__(self, attrs, tag, filename):
        message = f"{tag} requires the following attributes: {attrs}. Check {filename} for more info"
        super().__init__(message)
class MyParser(HTMLParser):

    def __init__(self, doc):
        self.doc = doc
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag=='iframe':
            for attr in attrs:
                if attr[0]=="width" or attr[0]=="height":
                    raise DisallowedAttributeException(attr, tag, self.doc)
        elif tag=='video':
            required_attrs = set([attr[0] for attr in attrs]) & set(REQUIRED_ATTRS_FOR_VIDEO)
            if (len(required_attrs)!=len(REQUIRED_ATTRS_FOR_VIDEO)):
                raise MissingAttributeException(REQUIRED_ATTRS_FOR_VIDEO, tag, self.doc)
        


BASE_PATH = "/home/rachel/rkaufman13-mysite"
list_of_files = os.listdir(f"{BASE_PATH}/_posts")
#list_of_files=['2025-08-25-reallist-nomination.md', '2024-06-05-fitbit-sdk-version-differences.markdown', '2024-08-14-command-line.md', '2025-03-31-google-sheets-java-sdk.md', '2025-06-23-partial-mocks.markdown', '2025-01-12-girl-geek.md', '2025-06-09-dont_sync_state.md', '2025-11-09-devtools-1.md', '2025-08-31-vavr-either-intro.md', '2024-01-14-game-jam-results.markdown', '2025-07-12-rakefiles.md', '2024-07-09-learnin-kube.markdown', '2025-03-17-overthewire-wargames.md', '2025-10-21-jekyll-site-data.md', '2024-12-21-why-blog.md', '2025-11-17-devtools-2.md', '2024-07-27-infinite-queens.md', '2025-04-13-leetcode.md', '2024-06-14-snowflake-stages.markdown', '2025-06-07-redesigning-bookguessr.md', '2024-12-01-advent-of-code-go.md', '2024-12-14-advent-of-code-day14.markdown', '2024-09-02-complete-rabbithole.md', '2024-11-04-what-is-webpack.md', '2024-12-30-building-good-habits.md', '2024-05-28-common-errors-with-fitbit-dev.markdown', '2024-06-30-fruit-tracker.markdown', '2024-10-07-queens-ai.markdown', '2025-01-30-google-hidden-options.md', '2025-01-28-reinforcement-learning-for-math-phobic.md', '2025-11-23-ai-documentation.md', '2025-11-18-speaking-panel-video.md', '2024-09-30-site-updates.md', '2025-03-12-girl-geek-talk.md', '2024-11-16-fck.md', '2025-10-04-accessibility-linter.md', '2025-03-26-status-code-division.md', '2023-11-22-welcome-to-jekyll.markdown', '2024-10-18-getting-unblocked-faster.md', '2024-05-05-firebase-crashlytics-and-feature-flags.markdown', '2024-12-08-composing-functions.markdown', '2025-01-10-skyline.md', '2025-06-16-ai-and-alt-text.markdown', '2025-09-25-watchman-watch-files.md', '2025-04-28-git-commit-hash.md', '2025-10-03-pyladies.md', '2025-09-15-momentum.md', '2025-09-05-codeword-announcement.md', '2025-06-28-reviewing-conferences.markdown', '2025-03-09-customizing-the-command-line.md', '2025-11-15-testing-philosophy.md', '2025-07-24-fastapi-and-nginx.markdown', '2024-04-12-local-firebase.markdown', '2024-01-31-typescript-and-noodle.markdown', '2024-05-24-fitbit-dev.markdown', '2025-05-01-podcast-appearance.md', '2023-11-27-electron.markdown', '2025-04-05-save-time-with-postman-pre-request.md', '2025-01-09-maze-generation.markdown']
#list_of_files=['2025-08-25-reallist-nomination.md','2024-06-05-fitbit-sdk-version-differences.markdown', '2024-08-14-command-line.md','2025-03-31-google-sheets-java-sdk.md', '2025-06-23-partial-mocks.markdown', '2025-01-12-girl-geek.md', '2025-06-09-dont_sync_state.md', '2025-11-09-devtools-1.md','2025-08-31-vavr-either-intro.md', '2024-01-14-game-jam-results.markdown', '2025-07-12-rakefiles.md', '2024-07-09-learnin-kube.markdown', '2025-03-17-overthewire-wargames.md', '2025-10-21-jekyll-site-data.md','2024-12-21-why-blog.md', '2025-11-17-devtools-2.md', '2024-07-27-infinite-queens.md', '2025-04-13-leetcode.md', '2024-06-14-snowflake-stages.markdown', '2025-06-07-redesigning-bookguessr.md', '2024-12-01-advent-of-code-go.md','2024-12-14-advent-of-code-day14.markdown', '2024-09-02-complete-rabbithole.md',  '2024-11-04-what-is-webpack.md', '2025-05-01-podcast-appearance.md',  '2024-12-30-building-good-habits.md', '2024-05-28-common-errors-with-fitbit-dev.markdown', '2024-06-30-fruit-tracker.markdown', '2024-10-07-queens-ai.markdown', '2025-01-30-google-hidden-options.md','2025-01-28-reinforcement-learning-for-math-phobic.md', '2025-11-23-ai-documentation.md', '2025-11-18-speaking-panel-video.md', '2024-09-30-site-updates.md', '2025-03-12-girl-geek-talk.md', '2024-11-16-fck.md','2025-10-04-accessibility-linter.md', '2025-03-26-status-code-division.md', '2023-11-22-welcome-to-jekyll.markdown', '2024-10-18-getting-unblocked-faster.md', '2024-05-05-firebase-crashlytics-and-feature-flags.markdown', '2024-12-08-composing-functions.markdown', '2025-01-10-skyline.md', '2025-06-16-ai-and-alt-text.markdown', '2025-09-25-watchman-watch-files.md', '2025-04-28-git-commit-hash.md', '2025-10-03-pyladies.md', '2025-09-15-momentum.md', '2025-09-05-codeword-announcement.md', '2025-06-28-reviewing-conferences.markdown', '2025-03-09-customizing-the-command-line.md', '2025-11-15-testing-philosophy.md','2025-07-24-fastapi-and-nginx.markdown', '2024-04-12-local-firebase.markdown', '2024-01-31-typescript-and-noodle.markdown', '2024-05-24-fitbit-dev.markdown', '2023-11-27-electron.markdown', '2025-04-05-save-time-with-postman-pre-request.md', '2025-01-09-maze-generation.markdown']

files_processed =0
for filename in list_of_files:
    try:
        with open(f"{BASE_PATH}/_posts/{filename}",'r') as content:
            parser = MyParser(filename)
            parser.feed(content.read())
            parser.close()
            files_processed+=1
    except DisallowedAttributeException as e:
        print(e)
        exit(1)
print(f"{files_processed} files out of {len(list_of_files)} processed.")
exit(0)
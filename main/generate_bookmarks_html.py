import time

playlist_file = 'playlist_names.txt'
html_file = 'bookmarks.html'

def load_playlist_names():
    with open(playlist_file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f]

def generate_bookmarks_html(playlist_names):
    html_content = [
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>',
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        '<TITLE>Bookmarks</TITLE>',
        '<H1>Bookmarks</H1>',
        '<DL><p>'
    ]

    timestamp = str(int(time.time()))

    for name in playlist_names:
        folder_html = (
            f'<DT><H3 ADD_DATE="{timestamp}" LAST_MODIFIED="{timestamp}">{name}</H3>\n'
            f'<DL><p>\n'
            f'<DT><A HREF="https://www.example.com/" ADD_DATE="{timestamp}" LAST_MODIFIED="{timestamp}">Placeholder</A>\n'
            f'</DL><p>'
        )
        html_content.append(folder_html)

    html_content.append('</DL><p>')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_content))

    print(f"Bookmarks HTML file has been created: {html_file}")

if __name__ == '__main__':
    playlist_names = load_playlist_names()
    generate_bookmarks_html(playlist_names)

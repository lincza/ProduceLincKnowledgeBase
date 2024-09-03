import os, frontmatter, re, json

root = 'articles'
structure_file = open('structure.json')
structure = json.load(structure_file)

items = []

sections = structure.get('articles')
for section in sections:
    section_path = os.path.join(root, section)
    areas = structure.get('articles').get(section)
    for area in areas:
        area_path = os.path.join(section_path, area)
        articles = structure.get('articles').get(section).get(area).get('files')
        if articles:
            for article in articles:
                article_path = os.path.join(area_path, article)
                article_file = open(article_path,'r')
                article_frontmatter = frontmatter.load(article_file)
                article_metadata = article_frontmatter.metadata
                item = {}
                item['title'] = article_metadata.get('title')
                item['path'] = article_path.replace(' ', '%20').replace('.md','')
                items.append(item)
        area_guides = []
        if 'Guides' in structure.get('articles').get(section).get(area):
            area_guides = structure.get('articles').get(section).get(area).get('Guides').get('files')
        if area_guides:
            for guide in area_guides:
                guide_path = os.path.join(area_path, 'Guides', guide)
                guide_file = open(guide_path,'r')
                guide_frontmatter = frontmatter.load(guide_file)
                guide_metadata = guide_frontmatter.metadata
                item = {}
                item['title'] = guide_metadata.get('title')
                item['path'] = guide_path.replace(' ', '%20').replace('.md','')
                items.append(item)

sections = structure.get('articles')
for section in sections:
    section_path = os.path.join(root, section)
    areas = structure.get('articles').get(section)
    for area in areas:
        area_path = os.path.join(section_path, area)
        articles = structure.get('articles').get(section).get(area).get('files')
        if articles:
            for article in articles:
                article_path = os.path.join(area_path, article)
                article_file = open(article_path,'r')
                article_file_content = article_file.read()
                article_file.close()
                text_in_brackets = re.findall(r'\[(.*?)\]', article_file_content)
                for text in text_in_brackets:
                    for item in items:
                        if text == item['title']:
                            article_file_content = article_file_content.replace('[' + text + ']', '[' + text + ']' + '(/' + item['path'] + ')')
                article_file = open(article_path,'w')
                article_file.write(article_file_content)
        area_guides = []
        if 'Guides' in structure.get('articles').get(section).get(area):
            area_guides = structure.get('articles').get(section).get(area).get('Guides').get('files')
        if area_guides:
            for guide in area_guides:
                guide_path = os.path.join(area_path, 'Guides', guide)
                guide_file = open(guide_path,'r')
                guide_file_content = guide_file.read()
                guide_file.close()
                text_in_brackets = re.findall(r'\[(.*?)\]', guide_file_content)
                for text in text_in_brackets:
                    for item in items:
                        if text == item['title']:
                            guide_file_content = guide_file_content.replace('[' + text + ']', '[' + text + ']' + '(/' + item['path'] + ')')
                guide_file = open(guide_path,'w')
                guide_file.write(guide_file_content)

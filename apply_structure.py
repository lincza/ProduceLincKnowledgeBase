import os, frontmatter, json

root = 'docs/articles'
structure_file = open('structure.json')
structure = json.load(structure_file)

sections = structure.get('articles')

section_start = 10000

for section in sections:
    section_start += 10000
    section_path = os.path.join(root, section)
    if not os.path.exists(section_path):
        os.makedirs(section_path)
    if not os.path.exists(os.path.join(section_path, 'index.md')):
        section_file = open(os.path.join(section_path, 'index.md'), 'w')
        section_file.close()
    section_file = open(os.path.join(section_path, 'index.md'), 'r')
    section_frontmatter = frontmatter.load(section_file)
    section_file.close()
    section_metadata = section_frontmatter.metadata
    section_metadata['layout'] = 'default'
    section_metadata['title'] = section
    section_metadata['nav_order'] = section_start
    section_metadata['has_children'] = True
    section_frontmatter.metadata = section_metadata
    section_file = open(os.path.join(section_path, 'index.md'), 'w')
    section_file.write(frontmatter.dumps(section_frontmatter))
    section_file.close()
    section_areas = structure.get('articles').get(section)
    area_start = section_start
    for area in section_areas:
        area_start += 1000
        area_path = os.path.join(section_path, area)
        if not os.path.exists(area_path):
            os.makedirs(area_path)
        if not os.path.exists(os.path.join(area_path, 'index.md')):
            area_file = open(os.path.join(area_path, 'index.md'), 'w')
            area_file.close()
        area_file = open(os.path.join(area_path, 'index.md'), 'r')
        area_frontmatter = frontmatter.load(area_file)
        area_file.close()
        area_metadata = area_frontmatter.metadata
        area_metadata['layout'] = 'default'
        area_metadata['title'] = area
        area_metadata['nav_order'] = area_start
        area_metadata['has_children'] = True
        area_metadata['parent'] = section
        area_frontmatter.metadata = area_metadata
        area_file = open(os.path.join(area_path, 'index.md'), 'w')
        area_file.write(frontmatter.dumps(area_frontmatter))
        area_file.close()
        area_articles = structure.get('articles').get(section).get(area).get('files')
        if area_articles:
            article_start = area_start
            for article in area_articles:
                article_start += 1
                article_path = os.path.join(area_path, article)
                if not os.path.exists(article_path):
                    article_file = open(article_path,'w')
                    article_file.close()
                article_file = open(article_path, 'r')
                article_frontmatter = frontmatter.load(article_file)
                article_file.close()
                article_metadata = article_frontmatter.metadata
                article_metadata['layout'] = 'default'
                article_metadata['title'] = article.replace('.md','')
                article_metadata['nav_order'] = article_start
                article_metadata['has_children'] = False
                article_metadata['parent'] = area
                article_metadata['grand_parent'] = section
                article_frontmatter.metadata = article_metadata
                article_file = open(article_path, 'w')
                article_file.write(frontmatter.dumps(article_frontmatter))
                article_file.close()
        if not os.path.exists(os.path.join(area_path,'Guides')):
            os.makedirs(os.path.join(area_path,'Guides'))
        if not os.path.exists(os.path.join(area_path, 'Guides', 'index.md')):
            guides_file = open(os.path.join(area_path, 'Guides', 'index.md'), 'w')
            guides_file.close()
        guides_file = open(os.path.join(area_path, 'Guides', 'index.md'), 'r')
        guides_frontmatter = frontmatter.load(guides_file)
        guides_file.close()
        guides_metadata = guides_frontmatter.metadata
        guides_metadata['layout'] = 'default'
        guides_metadata['title'] = 'Guides'
        guides_metadata['nav_order'] = area_start + 900
        guides_metadata['has_children'] = True
        guides_metadata['parent'] = area
        guides_metadata['grand_parent'] = section
        guides_frontmatter.metadata = guides_metadata
        guides_file = open(os.path.join(area_path, 'Guides', 'index.md'), 'w')
        guides_file.write(frontmatter.dumps(guides_frontmatter))
        guides_file.close()
        area_guides = []
        if 'Guides' in structure.get('articles').get(section).get(area):
            area_guides = structure.get('articles').get(section).get(area).get('Guides').get('files')
        if area_guides:
            guide_start = area_start + 900
            for guide in area_guides:
                guide_start += 1
                guide_path = os.path.join(area_path, 'Guides', guide)
                if not os.path.exists(guide_path):
                    guide_file = open(guide_path,'w')
                    guide_file.close()
                guide_file = open(guide_path, 'r')
                guide_frontmatter = frontmatter.load(guide_file)
                guide_file.close()
                guide_metadata = guide_frontmatter.metadata
                guide_metadata['layout'] = 'default'
                guide_metadata['title'] = guide.replace('.md','')
                guide_metadata['nav_order'] = guide_start
                guide_metadata['has_children'] = False
                guide_metadata['parent'] = 'Guides'
                guide_metadata['grand_parent'] = area
                guide_frontmatter.metadata = guide_metadata
                guide_file = open(guide_path, 'w')
                guide_file.write(frontmatter.dumps(guide_frontmatter))
                guide_file.close()


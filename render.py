from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Render pages
pages = [
    {'template': 'index.html', 'output': 'output/index.html'},

    {'template': 'education/hkust.html', 'output': 'output/education/hkust.html'},
    {'template': 'education/plktytc.html', 'output': 'output/education/plktytc.html'},

    {'template': 'experience/10botics.html', 'output': 'output/experience/10botics.html'},
    {'template': 'experience/hkust-ta.html', 'output': 'output/experience/hkust-ta.html'},

    {'template': 'robotics/robocon.html', 'output': 'output/robotics/robocon.html'},
    {'template': 'robotics/tyt-robotics.html', 'output': 'output/robotics/tyt-robotics.html'},
    
    {'template': 'projects/2v2-basketball.html', 'output': 'output/projects/2v2-basketball.html'},
    {'template': 'projects/calligraphy-robot.html', 'output': 'output/projects/calligraphy-robot.html'},
    {'template': 'projects/glyphmaster.html', 'output': 'output/projects/glyphmaster.html'},
    {'template': 'projects/index.html', 'output': 'output/projects/index.html'},
    {'template': 'projects/RDC2022_ARC.html', 'output': 'output/projects/RDC2022_ARC.html'},
    {'template': 'projects/RDC2022_TR.html', 'output': 'output/projects/RDC2022_TR.html'},
    {'template': 'projects/Robocon2023_trajplanner.html', 'output': 'output/projects/Robocon2023_trajplanner.html'},
    {'template': 'projects/Robocon2023_RR.html', 'output': 'output/projects/Robocon2023_RR.html'},
    {'template': 'projects/Robocon2024_R1.html', 'output': 'output/projects/Robocon2024_R1.html'},
    {'template': 'projects/Robocon2024_R2.html', 'output': 'output/projects/Robocon2024_R2.html'},
]

for page in pages:
    template = env.get_template(page['template'])
    output = template.render()
    with open(page['output'], 'w', encoding='utf-8') as f:
        f.write(output)
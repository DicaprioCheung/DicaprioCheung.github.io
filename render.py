from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Render pages
pages = [
    {'template': 'index.html', 'output': 'docs/index.html'},

    {'template': 'education/hkust.html', 'output': 'docs/education/hkust.html'},
    {'template': 'education/plktytc.html', 'output': 'docs/education/plktytc.html'},

    {'template': 'experience/10botics.html', 'output': 'docs/experience/10botics.html'},
    {'template': 'experience/hkust-ta.html', 'output': 'docs/experience/hkust-ta.html'},

    {'template': 'robotics/robocon.html', 'output': 'docs/robotics/robocon.html'},
    {'template': 'robotics/tyt-robotics.html', 'output': 'docs/robotics/tyt-robotics.html'},
    
    {'template': 'projects/2v2-basketball.html', 'output': 'docs/projects/2v2-basketball.html'},
    {'template': 'projects/calligraphy-robot.html', 'output': 'docs/projects/calligraphy-robot.html'},
    {'template': 'projects/glyphmaster.html', 'output': 'docs/projects/glyphmaster.html'},
    {'template': 'projects/index.html', 'output': 'docs/projects/index.html'},
    {'template': 'projects/RDC2022_ARC.html', 'output': 'docs/projects/RDC2022_ARC.html'},
    {'template': 'projects/RDC2022_TR.html', 'output': 'docs/projects/RDC2022_TR.html'},
    {'template': 'projects/Robocon2023_trajplanner.html', 'output': 'docs/projects/Robocon2023_trajplanner.html'},
    {'template': 'projects/Robocon2023_RR.html', 'output': 'docs/projects/Robocon2023_RR.html'},
    {'template': 'projects/Robocon2024_R1.html', 'output': 'docs/projects/Robocon2024_R1.html'},
    {'template': 'projects/Robocon2024_R2.html', 'output': 'docs/projects/Robocon2024_R2.html'},
    {'template': 'projects/robotic-arm-tic-tac-toe.html', 'output': 'docs/projects/robotic-arm-tic-tac-toe.html'},
]

for page in pages:
    template = env.get_template(page['template'])
    output = template.render()
    with open(page['output'], 'w', encoding='utf-8') as f:
        f.write(output)
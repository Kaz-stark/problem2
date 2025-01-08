from setuptools import find_packages, setup

package_name = 'problem2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kazu0709',
    maintainer_email='s23C1033WD@s.chibakoudai.jp',
    description='指定したファイルの最新更新日を提示します。',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_node = problem2.pub_node:main',
        ],
    },
)


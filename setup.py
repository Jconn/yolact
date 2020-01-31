from setuptools import setup

requirements = ["torch", "torchvision"]

package_name = 'yolactpy'


setup(
    name=package_name,
    version='0.0.1',
    packages=['yolact', 'yolact.data','yolact.layers','yolact.utils', 'yolact.scripts', 'yolact.layers.functions', 'yolact.layers.modules'],
    #py_modules=['yolact', 'backbone'],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Daniel Bolya',
    author_email='',
    description='yolact',
    license='MIT License',
)

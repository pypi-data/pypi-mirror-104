mpltw is a convience tool for using python's matplotlib module with tranditional Chinese word.

It simply do three things:
1. help you with downloading the Taipei Sans TC Beta (Regular) font in this module.
2. setup matplotlib to use this font as default.
3. add pyplot just for convience.

## How to install
You can use pip:

    pip install mpltw

Or from gitlab for master branch:
    
    pip install git+https://gitlab.com/scku208/matplotlib-taiwan-font

## How to use
    import mpltw
And then...

    from matplotlib import pyplot as plt
    plt.plot([1,2,3],[4,5,6], label='不用去記是prop...')
    plt.title('聽說其實台北黑體裡也有日文...您好/こんにちは')
    plt.xlabel('還是fontdict...')
    plt.text(1, 5,'text:亦或是fontproperties…')
    plt.annotate(r'annotation:通通都不用管了  \0皿0/耶～', xy=(2.5,5), xytext=(1.8,4.25),arrowprops=dict(facecolor='black', shrink=0.05))
    plt.legend() #這也是prop
    plt.show()
    
Or simply...

    from mpltw import plt 
    # using plt to do plotting things...
    
![demo plot](https://gitlab.com/scku208/matplotlib-taiwan-font/-/raw/master/demo.png)

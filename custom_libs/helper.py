import matplotlib.pyplot as plt;
import seaborn as sns;

binary_color=['steelblue', 'darksalmon']
single_color=['darksalmon']

def draw_barchart(df, key, binary):
    if binary:
        df[key].value_counts().plot(kind="bar", color=binary_color);
    else:    sns.histplot(df[key], kde=True, color='darksalmon', edgecolor='grey', alpha=0.7)

    plt.title('Histogram with Density Curve')
    plt.xlabel(key)
    plt.ylabel('Density')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
        df[key].value_counts().plot(kind="bar", color=single_color);

def draw_histogram_density_curve(df, key):


def draw_histogram(df, key):
    min_value = int(df[key].min())
    max_value = int(df[key].max())
    bins = range(min_value, max_value + 2)


    plt.hist(df[key], bins=bins, color='darksalmon', alpha=0.7, edgecolor='grey', rwidth=0.9, density=True)
    plt.xticks(bins)
    plt.title(f'Histogram of {key}')
    plt.xlabel(key)
    plt.ylabel('Frequency')
    plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.7, alpha=0.7)
    plt.show()

def value_count(df, key, value):
    # Total missing values
    return len(df[df[key] == value]) / len(df) * 100


if __name__ == '__main__':
    trash_can = ("Denis", True, 0)
    climate = (21, 53)

    cat_count, temperature, humidity = (trash_can + climate)[2:]
    print(cat_count, temperature, humidity)
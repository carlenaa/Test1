import os
import time
import csv
import datetime
import argparse
import sys
import math

#Custom Command
'''Terdiri dari program/function yang sebenarnya di ban, cuman dibuat ulang supaya kalau butuh, bisa tinggal panggil file ini'''


def uppercase(input_string): #Mengubah huruf jadi kapital semua
    result = ""
    for char in input_string:
        if 'a' <= char <= 'z': #Cek dia hurup kecil buakn
            result += chr(ord(char) - 32) #Mengubahnya ke kapital
        else:
            result += char #masukin kapital tsb ke variable
    return result

def bsort(arr): #bubble sort
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
def msort (arr): #merge sort
    
    def merge_sort(arr): #membagi dan menyatukan array
        if len(arr) <= 1:
            return arr

        # membagi arry jadi 2
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # rekursif
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        # menyatukan pembagian array tsb
        return merge(left_half, right_half)

    def merge(left, right): #membandingkan nilai indeks pada array
        merged = []
        left_index, right_index = 0, 0

        # membandingkan elemen kanan dan kiri teurs digabungin
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # append
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged
    
    sorted_arr = merge_sort(arr) #inisiasi fungsinya
    
    return sorted_arr

def take_name(uid, file_path): #Mengambil nama pemain dari uid
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if uid == row['id']:
                name = row['username']
                break
    return name

def find_id(id, file_path): #Melihat ketersediaan nama di database
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if id == row[0]:
                return True
    return False

def read_csv(file_path): #Membaca csv dan membuatnya dapat diakses seperti matrix (i.e: data[1][2])
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def take_role (uid, file_path): #mengambil role pemain dari uid
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if uid == row['id']:
                role = row['role']
                break
    return role

def from_x_take_y (uid, file_path, x, y): #mengambil x pemain dari uid
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if uid == row[x]:
                target = row[y]
                break
    return target

def capitalize_first_letter(input_string):
    result = ""
    for char in input_string[0]:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result+input_string[1:]

def update_csv(file_path, data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def save_updated_csv(file_path): #Save file csv yang sudah terupdate
    try:
        with open(file_path, 'r') as original_file:
            data = list(csv.reader(original_file))

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except Exception as e:
        print(f"An error occurred while saving the updated CSV file: {e}")
        print()
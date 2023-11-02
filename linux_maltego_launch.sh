#!/bin/bash

read -p "Please enter MPSIEM URL without https://: " url

export MPSIEM_URL="$url"

read -s -p "Please enter MPSIEM login: "$'\n' login

export MPSIEM_LOGIN="$login"

read -s -p "Please enter MPSIEM password: "$'\n' password

export MPSIEM_PASSWORD="$password"

maltego

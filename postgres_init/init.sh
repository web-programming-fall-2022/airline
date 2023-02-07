#!/bin/bash
set -e

export USER=$POSTGRES_USER
export PGPASSWORD=$POSTGRES_PASSWORD

if ! psql -lqt -U $USER | cut -d \| -f 1 | grep -qw ticket; then
  psql -U $USER -c "CREATE DATABASE ticket;"
  psql -U $USER -d ticket -a -f /app/ticket.sql
fi

if ! psql -lqt -U $USER | cut -d \| -f 1 | grep -qw auth; then
  psql -U $USER -c "CREATE DATABASE auth;"
fi
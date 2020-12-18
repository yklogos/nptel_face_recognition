import streamlit as st
import numpy as np
import pandas as pd 
import argparse
import os
from config import *
from model import predict

def main():
#     base_dir = args.base_dir
#     ver = args.ver
#     if base_dir is None:
#         base_dir = BASE_DIR

#     if ver is None:
#         ver = VER

    base_dir = os.getcwd()
    ver = VER

    st.title("Face Recognition on NPTEL vedios")
    # rad =st.sidebar.radio("Navigation",["predict","get vedios"])
    rad="predict"

    if rad=="predict":
        csv_files_dir = os.path.join(base_dir, 'data', 'csv_files')
        df = pd.read_csv(os.path.join(csv_files_dir, "vedio_metadata.csv"))

        channels_list = ["all"]+list(df.channel.unique())
        channel = st.sidebar.selectbox("channel_list", channels_list,index = 0)
        if channel!="all":
            playlist_list = ["all"]+list(df[df["channel"]==channel].playlist.unique())
        else:
            playlist_list = ["all"]+list(df.playlist.unique())

        playlist = st.sidebar.selectbox("playlist_list", playlist_list,index = 0)
        if playlist!="all":
            vedio_list = ["all"]+list(df[df["playlist"]==playlist].vedio.unique())
        else:
            vedio_list = ["all"]+list(df.vedio.unique())

        vedio = st.sidebar.selectbox("vedio", vedio_list, index = 1) ###
        vedio = "bcBrCQGI1tY.mp4" ###

        if vedio=="all":
            st.write("select one vedio")
        else:    
            vedio_path = df[df["vedio"]==vedio].iloc[0]["path"]
            predict(vedio_path, st, base_dir, ver)

# else if rad=="get vedios":

if __name__=='__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--base_dir', type=str, default=None, required=False, help='path to your base directory eg.\'D:\\nptel_face_recognition\'')
#     parser.add_argument('--ver', type=str, default=None, required=False, help='version of labelled images used eg. for known_faces2, ver=\'2\'')
#     args = parser.parse_args()
    main()
    
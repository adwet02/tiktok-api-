from TikTokApi import TikTokApi
import asyncio
import os

# ms_token = os.environ.get(
#     "ms_token", None
# )  # set your own ms_token, think it might need to have visited a profile

ms_token = "0QdUvPVvwN6eBDTnJNrA8PpwwaSDcI88jbmlJC5KndGERAEVI3CeA1OmQ8XIuB_bLXHm-IA1z-pC2KQPRYFaDquVAlmGsLMvDR5CgI_7gLvdxD3IrMx7D9q2aHi4FOAYUMDKyjnzOeD8xqWKTPZOuBI="

async def user_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))
        user = api.user("dipesh_ydv_07")
        user_data = await user.info()
        # print(user_data)
        user_info = user_data['userInfo']['user']
        context = {
            "pic" : user_info['avatarLarger'],
            "nickname" : user_info['nickname'],
            "id" : user_info['uniqueId'],
            "status" : user_info['verified'],

        }
        print(context)

        # async for video in user.videos(count=30):
        #     print(video)
        #     print(video.as_dict)

        # async for playlist in user.playlists():
        #     print(playlist)


if __name__ == "__main__":
    asyncio.run(user_example())



# from TikTokApi import TikTokApi

# api = TikTokApi()
# user = await api.user("dipesh_ydv_07").info()
# print(user)



# {'userInfo': {'stats': {}, 'statsV2': {}, 'user': {'avatarLarger': 'https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/efb543fe268155eae3e8a54f0e8ad377~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=14579&refresh_token=5b0fe132&x-expires=1747044000&x-signature=IpQaVuUAD5T7M12Eg55LxCBC13U%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=sg1', 
# 'avatarMedium': 'https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/efb543fe268155eae3e8a54f0e8ad377~tplv-tiktokx-cropcenter:720:720.jpeg?dr=14579&refresh_token=cfc80fe0&x-expires=1747044000&x-signature=GDhvaEeno7kr8xftXbQjQAS17iw%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=sg1',
#  'avatarThumb': 'https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/efb543fe268155eae3e8a54f0e8ad377~tplv-tiktokx-cropcenter:100:100.jpeg?dr=14579&refresh_token=2f6869cf&x-expires=1747044000&x-signature=3mj7XiK0fmDiwOMkYtN%2Bd7Qh1yw%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=sg1', 'canExpPlaylist': True, 'commentSetting': 0, 'commerceUserInfo': {'commerceUser': False}, 'downloadSetting': 3, 'duetSetting': 0, 'followingVisibility': 2, 'ftc': False, 'id': '7227107624393868290', 'isADVirtual': False, 'isEmbedBanned': False, 'nickNameModifyTime': 1725614734, 
#  'nickname': 'Heyy! Pretty Strangers👋', 'openFavorite': False, 'privateAccount': False, 'profileEmbedPermission': 1, 'profileTab': {'showPlayListTab': False, 'showQuestionTab': True}, 'relation': 0, 'secUid': 'MS4wLjABAAAAOM_wqX0WVa4caUin5hNaHrzhnfCVrW6Qp8kTEgvDkavbTDnYn38qApD9NfHCkCNT', 'secret': False, 'signature': 'EVERYONE WILL COME TO MY FUNERAL TO  MAKE SURE THAT I STAY DEAD ⚓', 'stitchSetting': 0, 'ttSe
# ller': False, 'uniqueId': 'dipesh_ydv_07', 'verified': False}}}
# userInfo.user.avatarLarger
# userInfo.user.nickname
# userInfo.user.uniqueId
# userInfo.user.verified


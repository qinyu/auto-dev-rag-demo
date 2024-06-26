Feature: 上传生活视频
  作为 InnoRev 网站的用户
  我想上传我的生活视频到网站上
  以便展示给其他用户

  Scenario: 上传视频格式限制
    Given 用户上传的视频格式不符合要求
    When 用户上传视频时其格式不符合要求
    Then 系统将提示用户需要上传正确格式的视频

  Scenario: 上传视频过大
    Given 用户上传的视频过大
    When 用户上传比网站规定大小还要大的视频文件
    Then 系统将提示用户需要上传符合规定大小的视频文件

  Scenario: 上传视频失败
    Given 网络故障或者其他原因导致用户上传视频失败
    When 上传失败时
    Then 系统将提示用户失败的原因，并给予技术支持或者帮助文档供用户修复错误。
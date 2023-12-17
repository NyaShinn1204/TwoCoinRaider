import tkinter as tk

class Setting:
  tokens = []
  voicefile = []
  validtoken = 0
  invalidtoken = 0
  lockedtoken = 0
  
  # enabled ck.button
  proxy_enabled = tk.BooleanVar()
  proxy_enabled.set(False)
  
  token_filenameLabel = tk.StringVar()
  token_filenameLabel.set("")
  totaltokenLabel = tk.StringVar()
  totaltokenLabel.set("Total: 000")
  validtokenLabel = tk.StringVar()
  validtokenLabel.set("Valid: 000")
  invalidtokenLabel = tk.StringVar()
  invalidtokenLabel.set("Invalid: 000")
  lockedtokenLabel = tk.StringVar()
  lockedtokenLabel.set("Locked: 000")
  
  proxytype = tk.StringVar()
  proxytype.set("http")
  proxies = []
  totalproxies = 0
  vaildproxies = 0
  invaildproxies = 0

  proxysetting = tk.BooleanVar()
  proxysetting.set(False)

  proxy_filenameLabel = tk.StringVar()
  proxy_filenameLabel.set("")
  totalProxiesLabel = tk.StringVar()
  totalProxiesLabel.set("Total: 000")
  validProxiesLabel = tk.StringVar()
  validProxiesLabel.set("Valid: 000")
  invalidProxiesLabel = tk.StringVar()
  invalidProxiesLabel.set("Invalid: 000")
  
  voicefile_filenameLabel = tk.StringVar()
  voicefile_filenameLabel.set("")
  
  # joiner
  suc_joiner_Label = tk.StringVar()
  suc_joiner_Label.set("Success: 000")
  fai_joiner_Label = tk.StringVar()
  fai_joiner_Label.set("Failed: 000")
  
  # leaver
  suc_leaver_Label = tk.StringVar()
  suc_leaver_Label.set("Success: 000")
  fai_leaver_Label = tk.StringVar()
  fai_leaver_Label.set("Failed: 000")
  
  # vc joiner
  suc_vcjoiner_Label = tk.StringVar()
  suc_vcjoiner_Label.set("Success: 000")
  fai_vcjoiner_Label = tk.StringVar()
  fai_vcjoiner_Label.set("Failed: 000")

  # vc leaver
  suc_vcleaver_Label = tk.StringVar()
  suc_vcleaver_Label.set("Success: 000")
  fai_vcleaver_Label = tk.StringVar()
  fai_vcleaver_Label.set("Failed: 000")  

  # nm spam
  suc_nmspam_Label = tk.StringVar()
  suc_nmspam_Label.set("Success: 000")
  fai_nmspam_Label = tk.StringVar()
  fai_nmspam_Label.set("Failed: 000")
  
  # reply spam
  suc_replyspam_Label = tk.StringVar()
  suc_replyspam_Label.set("Success: 000")
  fai_replyspam_Label = tk.StringVar()
  fai_replyspam_Label.set("Failed: 000")
  
  # ticket spam
  suc_ticketspam_Label = tk.StringVar()
  suc_ticketspam_Label.set("Success: 000")
  fai_ticketspam_Label = tk.StringVar()
  fai_ticketspam_Label.set("Failed: 000")
  
  # vc spam
  suc_vcspam_Label = tk.StringVar()
  suc_vcspam_Label.set("Success: 000")
  fai_vcspam_Label = tk.StringVar()
  fai_vcspam_Label.set("Failed: 000")
  
  # slash spam
  suc_shspam_Label = tk.StringVar()
  suc_shspam_Label.set("Success: 000")
  fai_shspam_Label = tk.StringVar()
  fai_shspam_Label.set("Failed: 000")
  
  # reaction spam
  suc_reactionspam_Label = tk.StringVar()
  suc_reactionspam_Label.set("Success: 000")
  fai_reactionspam_Label = tk.StringVar()
  fai_reactionspam_Label.set("Failed: 000")
  
  # threads spam
  suc_threadsspam_Label = tk.StringVar()
  suc_threadsspam_Label.set("Success: 000")
  fai_threadsspam_Label = tk.StringVar()
  fai_threadsspam_Label.set("Failed: 000")
  
  spam_allping = tk.BooleanVar()
  spam_allping.set(False)
  spam_allch = tk.BooleanVar()
  spam_allch.set(False)
  spam_rdstring = tk.BooleanVar()
  spam_rdstring.set(False)
  spam_ratefixer = tk.BooleanVar()
  spam_ratefixer.set(False)
  spam_randomconvert = tk.BooleanVar()
  spam_randomconvert.set(False)

  reply_allping = tk.BooleanVar()
  reply_allping.set(False)
  reply_allmg = tk.BooleanVar()
  reply_allmg.set(False)
  reply_rdstring = tk.BooleanVar()
  reply_rdstring.set(False)
  reply_ratefixer = tk.BooleanVar()
  reply_ratefixer.set(False)
  
  ticket_ratefixer = tk.BooleanVar()
  ticket_ratefixer.set(False) 
  
  slash_ratefixer = tk.BooleanVar()
  slash_ratefixer.set(False) 
  
  sbspam_rdsounds = tk.BooleanVar()
  sbspam_rdsounds.set(False)
  
  delay01_01 = tk.DoubleVar()
  delay01_01.set(0.1)
  
  delay01_02 = tk.DoubleVar()
  delay01_02.set(0.1)
  
  delay01_03 = tk.DoubleVar()
  delay01_03.set(0.1)

  delay01_04 = tk.DoubleVar()
  delay01_04.set(0.1)
  
  delay02_01 = tk.DoubleVar()
  delay02_01.set(0.1)

  delay02_02 = tk.DoubleVar()
  delay02_02.set(0.1)

  delay02_03 = tk.DoubleVar()
  delay02_03.set(0.1)

  delay02_04 = tk.DoubleVar()
  delay02_04.set(0.1)

  delay02_05 = tk.DoubleVar()
  delay02_05.set(0.1)

  delay02_06 = tk.DoubleVar()
  delay02_06.set(0.1)

  delay99_01 = tk.DoubleVar()
  delay99_01.set(0.1)

  delay99_02 = tk.DoubleVar()
  delay99_02.set(0.1)

  mention_count_def = tk.DoubleVar()
  mention_count_def.set(20)
  
  joiner_link = tk.StringVar()
  joiner_link.set("")
  bypass_ms = tk.BooleanVar()
  bypass_ms.set(False)
  bypass_cap = tk.BooleanVar()
  bypass_cap.set(False)
  delete_join_ms = tk.BooleanVar()
  delete_join_ms.set("False")
  joiner_serverid = tk.StringVar()
  joiner_serverid.set("")
  joiner_channelid = tk.StringVar()
  joiner_channelid.set("")
  leaver_serverid = tk.StringVar()
  leaver_serverid.set("")
  vcjoin_channelid = tk.StringVar()
  vcjoin_channelid.set("")
  vcjoin_serverid = tk.StringVar()
  vcjoin_serverid.set("")
  vcleave_channelid = tk.StringVar()
  vcleave_channelid.set("")
  vcleave_serverid = tk.StringVar()
  vcleave_serverid.set("")
  spam_serverid = tk.StringVar()
  spam_serverid.set("")
  spam_channelid = tk.StringVar()
  spam_channelid.set("")
  reply_serverid = tk.StringVar()
  reply_serverid.set("")
  reply_channelid = tk.StringVar()
  reply_channelid.set("")
  reply_messageid = tk.StringVar()
  reply_messageid.set("")
  vcspam_serverid = tk.StringVar()
  vcspam_serverid.set("")
  vcspam_channelid = tk.StringVar()
  vcspam_channelid.set("")
  sbspam_serverid = tk.StringVar()
  sbspam_serverid.set("")
  sbspam_channelid = tk.StringVar()
  sbspam_channelid.set("")
  ticket_serverid = tk.StringVar()
  ticket_serverid.set("")
  ticket_channelid = tk.StringVar()
  ticket_channelid.set("")
  ticket_messageid = tk.StringVar()
  ticket_messageid.set("")
  slash_serverid = tk.StringVar()
  slash_serverid.set("")
  slash_channelid = tk.StringVar()
  slash_channelid.set("")
  slash_applicationid = tk.StringVar()
  slash_applicationid.set("")
  slash_commandname = tk.StringVar()
  slash_commandname.set("")
  slash_subcommandname = tk.StringVar()
  slash_subcommandname.set("")
  slash_subcommandname_value = tk.StringVar()
  slash_subcommandname_value.set("")
  reaction_channelid = tk.StringVar()
  reaction_channelid.set("")
  reaction_messageid = tk.StringVar()
  reaction_messageid.set("")
  reaction_emoji = tk.StringVar()
  reaction_emoji.set("")
  threads_channelid = tk.StringVar()
  threads_channelid.set("")
  threads_name = tk.StringVar()
  threads_name.set("")
  
  theme_var = tk.StringVar(value="Default Theme")

class SettingVariable:
  joinerresult_success = 0
  joinerresult_failed = 0
  leaverresult_success = 0
  leaverresult_failed = 0
  nmspamresult_success = 0
  nmspamresult_failed = 0
  vcjoinerresult_success = 0
  vcjoinerresult_failed = 0
  vcleaverresult_success = 0
  vcleaverresult_failed = 0
  replyspamresult_success = 0
  replyspamresult_failed = 0
  ticketspamresult_success = 0
  ticketspamresult_failed = 0
  slashspamresult_success = 0
  slashspamresult_failed = 0
  vcspamresult_success = 0
  vcspamresult_failed = 0
  
class oldSetting:
  tokens = []
  validtoken = 0
  invalidtoken = 0
  lockedtoken = 0
  
  # enabled ck.button
  proxy_enabled = tk.BooleanVar()
  proxy_enabled.set(False)
  
  token_filenameLabel = tk.StringVar()
  token_filenameLabel.set("")
  totaltokenLabel = tk.StringVar()
  totaltokenLabel.set("Total: 000")
  validtokenLabel = tk.StringVar()
  validtokenLabel.set("Valid: 000")
  invalidtokenLabel = tk.StringVar()
  invalidtokenLabel.set("Invalid: 000")
  lockedtokenLabel = tk.StringVar()
  lockedtokenLabel.set("Locked: 000")
  
  proxytype = tk.StringVar()
  proxytype.set("http")
  proxies = []
  totalproxies = 0
  vaildproxies = 0
  invaildproxies = 0

  proxysetting = tk.BooleanVar()
  proxysetting.set(False)

  proxy_filenameLabel = tk.StringVar()
  proxy_filenameLabel.set("")
  totalProxiesLabel = tk.StringVar()
  totalProxiesLabel.set("Total: 000")
  validProxiesLabel = tk.StringVar()
  validProxiesLabel.set("Valid: 000")
  invalidProxiesLabel = tk.StringVar()
  invalidProxiesLabel.set("Invalid: 000")
  
  voicefile_filenameLabel = tk.StringVar()
  voicefile_filenameLabel.set("")
  
  # joiner
  suc_joiner_Label = tk.StringVar()
  suc_joiner_Label.set("Success: 000")
  fai_joiner_Label = tk.StringVar()
  fai_joiner_Label.set("Failed: 000")
  
  # leaver
  suc_leaver_Label = tk.StringVar()
  suc_leaver_Label.set("Success: 000")
  fai_leaver_Label = tk.StringVar()
  fai_leaver_Label.set("Failed: 000")
  
  # vc joiner
  suc_vcjoiner_Label = tk.StringVar()
  suc_vcjoiner_Label.set("Success: 000")
  fai_vcjoiner_Label = tk.StringVar()
  fai_vcjoiner_Label.set("Failed: 000")

  # vc leaver
  suc_vcleaver_Label = tk.StringVar()
  suc_vcleaver_Label.set("Success: 000")
  fai_vcleaver_Label = tk.StringVar()
  fai_vcleaver_Label.set("Failed: 000")  

  # nm spam
  suc_nmspam_Label = tk.StringVar()
  suc_nmspam_Label.set("Success: 000")
  fai_nmspam_Label = tk.StringVar()
  fai_nmspam_Label.set("Failed: 000")
  
  # reply spam
  suc_replyspam_Label = tk.StringVar()
  suc_replyspam_Label.set("Success: 000")
  fai_replyspam_Label = tk.StringVar()
  fai_replyspam_Label.set("Failed: 000")
  
  # ticket spam
  suc_ticketspam_Label = tk.StringVar()
  suc_ticketspam_Label.set("Success: 000")
  fai_ticketspam_Label = tk.StringVar()
  fai_ticketspam_Label.set("Failed: 000")
  
  # vc spam
  suc_vcspam_Label = tk.StringVar()
  suc_vcspam_Label.set("Success: 000")
  fai_vcspam_Label = tk.StringVar()
  fai_vcspam_Label.set("Failed: 000")
  
  # slash spam
  suc_shspam_Label = tk.StringVar()
  suc_shspam_Label.set("Success: 000")
  fai_shspam_Label = tk.StringVar()
  fai_shspam_Label.set("Failed: 000")
  
  # reaction spam
  suc_reactionspam_Label = tk.StringVar()
  suc_reactionspam_Label.set("Success: 000")
  fai_reactionspam_Label = tk.StringVar()
  fai_reactionspam_Label.set("Failed: 000")
  
  # token onliner
  suc_tokenonliner_Label = tk.StringVar()
  suc_tokenonliner_Label.set("Success: 000")
  fai_tokenonliner_Label = tk.StringVar()
  fai_tokenonliner_Label.set("Failed: 000")
  
  spam_allping = tk.BooleanVar()
  spam_allping.set(False)
  spam_allch = tk.BooleanVar()
  spam_allch.set(False)
  spam_rdstring = tk.BooleanVar()
  spam_rdstring.set(False)
  spam_ratefixer = tk.BooleanVar()
  spam_ratefixer.set(False)
  spam_randomconvert = tk.BooleanVar()
  spam_randomconvert.set(False)

  reply_allping = tk.BooleanVar()
  reply_allping.set(False)
  reply_allmg = tk.BooleanVar()
  reply_allmg.set(False)
  reply_rdstring = tk.BooleanVar()
  reply_rdstring.set(False)
  reply_ratefixer = tk.BooleanVar()
  reply_ratefixer.set(False)
  
  ticket_ratefixer = tk.BooleanVar()
  ticket_ratefixer.set(False) 
  
  slash_ratefixer = tk.BooleanVar()
  slash_ratefixer.set(False) 
  
  sbspam_rdsounds = tk.BooleanVar()
  sbspam_rdsounds.set(False)
  
  delay01 = tk.DoubleVar()
  delay01.set(0.1)
  
  delay02 = tk.DoubleVar()
  delay02.set(0.1)
  
  delay03 = tk.DoubleVar()
  delay03.set(0.1)
    
  delay04 = tk.DoubleVar()
  delay04.set(0.1)
  
  delay05 = tk.DoubleVar()
  delay05.set(0.1)
  
  delay91 = tk.DoubleVar()
  delay91.set(0.1)
  
  mention_count_def = tk.DoubleVar()
  mention_count_def.set(20)
  
  joiner_link = tk.StringVar()
  joiner_link.set("")
  bypass_ms = tk.BooleanVar()
  bypass_ms.set(False)
  bypass_cap = tk.BooleanVar()
  bypass_cap.set(False)
  delete_join_ms = tk.BooleanVar()
  delete_join_ms.set("False")
  joiner_serverid = tk.StringVar()
  joiner_serverid.set("")
  joiner_channelid = tk.StringVar()
  joiner_channelid.set("")
  leaver_serverid = tk.StringVar()
  leaver_serverid.set("")
  vcjoin_channelid = tk.StringVar()
  vcjoin_channelid.set("")
  vcjoin_serverid = tk.StringVar()
  vcjoin_serverid.set("")
  vcleave_channelid = tk.StringVar()
  vcleave_channelid.set("")
  vcleave_serverid = tk.StringVar()
  vcleave_serverid.set("")
  spam_serverid = tk.StringVar()
  spam_serverid.set("")
  spam_channelid = tk.StringVar()
  spam_channelid.set("")
  reply_serverid = tk.StringVar()
  reply_serverid.set("")
  reply_channelid = tk.StringVar()
  reply_channelid.set("")
  reply_messageid = tk.StringVar()
  reply_messageid.set("")
  vcspam_serverid = tk.StringVar()
  vcspam_serverid.set("")
  vcspam_channelid = tk.StringVar()
  vcspam_channelid.set("")
  sbspam_serverid = tk.StringVar()
  sbspam_serverid.set("")
  sbspam_channelid = tk.StringVar()
  sbspam_channelid.set("")
  ticket_serverid = tk.StringVar()
  ticket_serverid.set("")
  ticket_channelid = tk.StringVar()
  ticket_channelid.set("")
  ticket_messageid = tk.StringVar()
  ticket_messageid.set("")
  slash_serverid = tk.StringVar()
  slash_serverid.set("")
  slash_channelid = tk.StringVar()
  slash_channelid.set("")
  slash_applicationid = tk.StringVar()
  slash_applicationid.set("")
  slash_commandname = tk.StringVar()
  slash_commandname.set("")
  slash_subcommandname = tk.StringVar()
  slash_subcommandname.set("")
  slash_subcommandname_value = tk.StringVar()
  slash_subcommandname_value.set("")
  reaction_channelid = tk.StringVar()
  reaction_channelid.set("")
  reaction_messageid = tk.StringVar()
  reaction_messageid.set("")
  reaction_emoji = tk.StringVar()
  reaction_emoji.set("")
  
  voicefile = []
  
class oldSettingVariable:
  joinerresult_success = 0
  joinerresult_failed = 0
  leaverresult_success = 0
  leaverresult_failed = 0
  nmspamresult_success = 0
  nmspamresult_failed = 0
  vcjoinerresult_success = 0
  vcjoinerresult_failed = 0
  vcleaverresult_success = 0
  vcleaverresult_failed = 0
  replyspamresult_success = 0
  replyspamresult_failed = 0
  ticketspamresult_success = 0
  ticketspamresult_failed = 0
  slashspamresult_success = 0
  slashspamresult_failed = 0
  vcspamresult_success = 0
  vcspamresult_failed = 0
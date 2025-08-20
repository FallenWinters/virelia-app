def assign_badge(petition_count):
  if petition_count>=10:
      return "gold badge: signed 10 petitions"
  elif petiton_count>=5:
    return "silver badge: signed 5 petition"
  elif petition_count>=1:
    return "bronze badge: signed 1 petition"
  else:
    return "no badge: no petitions signed"

#example usage
user_petition_count = 7
badge = assign_badge(user_petition_count)print(badge)

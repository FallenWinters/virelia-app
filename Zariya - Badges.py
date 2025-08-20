def assign_badge(petition_count):
  if petition_count>=10:
      return "gold badge: signed 10 petitions"
  elif petition_count>=5:
    return "silver badge: signed 5 petitions"
  elif petition_count>=1:
    return "bronze badge: signed 1 petition"
  else:
    return "no badge: no petitions signed"
